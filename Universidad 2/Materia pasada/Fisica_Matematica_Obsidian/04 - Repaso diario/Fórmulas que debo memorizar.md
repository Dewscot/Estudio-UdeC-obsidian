# Fórmulas que debo memorizar

## Serie geométrica
$$
\sum_{n=0}^{\infty} r^n=\frac{1}{1-r}, \quad |r|<1
$$

## Armónica general
$$
\sum_{n=1}^{\infty}\frac{1}{n^\alpha}
$$

Converge si \(\alpha>1\).

## Taylor
$$
f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n
$$

## Fourier
$$
f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}
\left[
a_n\cos\left(\frac{2\pi n}{T}x\right)
+
b_n\sin\left(\frac{2\pi n}{T}x\right)
\right]
$$

## Parseval
$$
\frac{1}{T}\int_0^T |f(x)|^2\,dx
=
\frac{a_0^2}{4}
+
\frac{1}{2}\sum_{n=1}^{\infty}(a_n^2+b_n^2)
$$
