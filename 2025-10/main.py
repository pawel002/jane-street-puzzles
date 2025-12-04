import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize_scalar

EPS = 1e-12


def q(p):
    V = np.zeros((5, 5), dtype=float)
    Q = np.zeros((5, 5), dtype=float)

    V[4, :] = 1.0
    V[:, 3] = 0.0
    Q[3, 2] = 1.0

    for b in range(3, -1, -1):
        for s in range(2, -1, -1):
            x11 = V[b, s + 1]
            x12 = V[b + 1, s]
            x21 = 4 * p + (1 - p) * V[b, s + 1]
            x22 = V[b, s + 1]

            # minimax (pure saddle?)
            row_mins = [min(x11, x12), min(x21, x22)]
            col_maxs = [max(x11, x21), max(x12, x22)]
            v_lower = max(row_mins)
            v_upper = min(col_maxs)
            delta = x11 + x22 - x12 - x21

            # choose (x,y): x=P(Wait), y=P(Strike)
            if abs(v_lower - v_upper) < EPS:
                if abs(v_lower - x11) < EPS:
                    x, y, V[b, s] = 1.0, 1.0, x11
                elif abs(v_lower - x12) < EPS:
                    x, y, V[b, s] = 1.0, 0.0, x12
                elif abs(v_lower - x21) < EPS:
                    x, y, V[b, s] = 0.0, 1.0, x21
                else:
                    x, y, V[b, s] = 0.0, 0.0, x22

            else:
                x = (x22 - x21) / delta
                y = (x22 - x12) / delta
                x = min(max(x, 0.0), 1.0)
                y = min(max(y, 0.0), 1.0)
                V[b, s] = (x11 * x22 - x12 * x21) / delta

            if not (b == 3 and s == 2):
                Q[b, s] = Q[b + 1, s] * x * (1 - y) + Q[b, s + 1] * (
                    x * y + (1 - x) * (1 - y) + (1 - x) * y * (1 - p)
                )

    return Q[0, 0]


xs = np.linspace(0, 1, 1000)
ys = [q(float(x)) for x in xs]

res = minimize_scalar(
    lambda x: -q(x),
    bounds=(0.0, 1.0),
    method="bounded",
    options={"xatol": 1e-12, "maxiter": 1000},
)
p_star = res.x
q_star = q(p_star)
print(res.nfev, res.status, res.message)
print(f"p* ≈ {p_star:.15f},  q(p*) ≈ {q_star:.15f}")

plt.figure(p_star)
plt.plot(xs, ys)
plt.vlines(x=res.x, ymin=0, ymax=0.3, color="r")
plt.text(x=p_star, y=q_star, s=f"q(p*) ≈ {q_star:.15f}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("f(x) on [0, 1]")
plt.xlim(0.0, 1.0)
plt.grid(True)
plt.show()
