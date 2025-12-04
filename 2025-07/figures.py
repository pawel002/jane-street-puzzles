import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# figure 1
fig, ax = plt.subplots(figsize=(5, 5))
alpha = 1.35

for y in [1, alpha, 2]:
    ax.hlines(y, 0, 3, linestyles='dashed', linewidth=0.8)
for x in [1, alpha, 2]:
    ax.vlines(x, 0, 3, linestyles='dashed', linewidth=0.8)

ax.plot([1, 2], [1, 2], color='black', linewidth=1.2)

lower_triangle = Polygon([[1, 1], [1, alpha], [alpha, alpha]], closed=True, fill=False, hatch='//', linewidth=1.2, color='r')
upper_triangle = Polygon([[alpha, alpha], [alpha, 2], [2, 2]], closed=True, fill=False, hatch='//', linewidth=1.2, color='b')
ax.add_patch(lower_triangle)
ax.add_patch(upper_triangle)

ax.text(0.7, alpha, r"$a$", fontsize=12, va='bottom')
ax.text(alpha, 0.7, r"$a$", fontsize=12, ha='left')
ax.text(1.25, 1.15, r"$a>v_1>v_2$", fontsize=12, color='red')
ax.text(1.5, 1.4, r"$v_1>v_2>a$", fontsize=12, color='blue')

ax.set_xticks([1, 2])
ax.set_yticks([1, 2])
ax.set_xlabel(r"$v_2$")
ax.set_ylabel(r"$v_1$")
ax.set_xlim(0.75, 2.25)
ax.set_ylim(0.75, 2.25)

ax.set_aspect('equal', adjustable='box')
plt.tight_layout()
plt.savefig("res/figure1.png")
plt.close()

# figure 2
fig, ax = plt.subplots(figsize=(5, 5))

v2, v3 = 1.8, 1.1
x = [0, 1, 2, 3, 4]
y = [v2, v2, v3, v2, v2]
ax.plot(x, y, color='black', linewidth=1.2)
ax.hlines(v3, 0, 4, linestyles='dashed', linewidth=0.8)

for y in [1, 2, 3]:
    ax.vlines(y, 0, 2.5, linestyles='dashed', linewidth=0.8)

triangle = Polygon([[1, v2], [2, v3], [3, v2]], closed=True, fill=False, hatch='//', linewidth=1.2, color='r')
ax.add_patch(triangle)

ax.text(2, v2+0.1, "LOST DISTANCE", fontsize=12, color='red')

ax.set_xlim(0, 4)
ax.set_ylim(0, 2.3)
ax.set_xticks([1, 2, 3])
ax.set_yticks([v2, v3])
ax.set_xticklabels([r"$t_0$", r"$t_0+t_s$", r"$t_0+2t_s$"])
ax.set_yticklabels([r"$v_2$", r"$v_3$"])

ax.set_aspect('equal', adjustable='box')
plt.tight_layout()
plt.savefig("res/figure2.png")
plt.close()