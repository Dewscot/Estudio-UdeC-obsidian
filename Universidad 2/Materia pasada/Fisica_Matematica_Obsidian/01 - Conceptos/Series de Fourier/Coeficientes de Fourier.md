# Coeficientes de Fourier

## Serie trigonométrica
$$
f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}
\left[
a_n\cos\left(\frac{2\pi n}{T}x\right)
+
b_n\sin\left(\frac{2\pi n}{T}x\right)
\right]
$$

## Coeficientes
$$
a_n = \frac{2}{T}\int_0^T f(x)\cos\left(\frac{2\pi n}{T}x\right)dx
$$

$$
b_n = \frac{2}{T}\int_0^T f(x)\sin\left(\frac{2\pi n}{T}x\right)dx
$$

## Atajo por simetría
- Si $f(x)$ es par, entonces $b_n = 0$.
- Si $f(x)$ es impar, entonces $a_n = 0$.

## Conexiones
- [[Funciones ortogonales]]
- [[Condiciones de Dirichlet]]
- [[Funciones pares e impares]]

