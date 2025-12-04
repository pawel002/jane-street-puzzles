### Solution

Consider the probability of the path without any ones dependent on $p$ to be $f(p)$. We see that if the tree is infinite, we can suppose that given a root and two subtrees, those subtrees have the same characteristics as the main tree.

Lets label the probability of the path existing with at most one "1" to be $g(p)$. The probability of tree having a path with zero "1"s is $f(p)$. For the path to exist, at least one subtree should have the path, so we get the equation:

$$
f(p) = p(2f(p)(1-f(p)) + f^2(p)) = p(2f(p) - f^2(p)) \implies f(p) = 2 - \frac{1}{p}
$$

Now we see that the probability of the main tree having at most one $1$ is the probability that we get "0" in the root (which is $p$), and at least one subtree with at most one "1" OR we get "1" in the root (with prob $1-p$) and we need to get two trees with "0" paths. This yields:

$$
g(p) = p \Big(2g(p) - g^2(p) \Big) + (1-p) \Big(2f(p) - f^2(p) \Big).
$$

We need to find such $p_0$ that $g(p_0) = \frac{1}{2}$. Plugging it in, we get:

$$
\begin{align*}
    \frac{1}{2} &= \frac{3}{4}p_0 + (1 - p_0)\Big(\frac{2}{p_0} - \frac{1}{p_0^2} \Big) \\
    p_0 &= 0.530604.
\end{align*}
$$
