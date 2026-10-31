---
tags:
  - concepto
  - calculo-iv
  - numeros-complejos
tipo: concepto
asignatura: "Cálculo IV"
unidad: "Semana 1 — Números complejos"
estado: pendiente
fuente: "Apunte del profesor: Semana1-1.pdf, pp. 9-11"
---

> [!abstract] Pregunta central
> ¿Cómo permite la forma polar interpretar y calcular productos y potencias de números complejos?

## 1. Idea e interpretación intuitiva

La representación cartesiana $x+iy$ destaca las componentes; la polar $re^{i\theta}$ destaca **distancia al origen** y **dirección**. En forma polar, multiplicar números complejos significa multiplicar módulos y sumar ángulos.

## 2. Fundamentos, hipótesis y convenciones

- Para $z=x+iy\neq0$, $r=|z|>0$, $x=r\cos\theta$, $y=r\sin\theta$.
- **Argumentos:** si $\theta$ es argumento de $z$, también lo es $\theta+2\pi k$, $k\in\mathbb Z$.
- **Convención de Semana 1:** se toma un argumento principal $\operatorname{Arg}(z)\in(-\pi,\pi]$. En la nota [[Logaritmo complejo y ramas]] se utiliza la rama abierta $(-\pi,\pi)$ sobre un dominio cortado: son contextos distintos.
- $e^{i\theta}=\cos\theta+i\sin\theta$.

## 3. Desarrollo matemático o procedimiento

Por la sustitución de coordenadas,

$$
z=x+iy=r(\cos\theta+i\sin\theta)=\boxed{re^{i\theta}}.
$$

Si $z_1=r_1e^{i\theta_1}$ y $z_2=r_2e^{i\theta_2}$,

$$
\boxed{z_1z_2=r_1r_2e^{i(\theta_1+\theta_2)}}.
$$

Por iteración,

$$
\boxed{z^n=r^ne^{in\theta}},\qquad n\in\mathbb N.
$$

Para $z\neq0$, $z^{-1}=r^{-1}e^{-i\theta}$; la división resta argumentos.

**Ejemplo del apunte:** $\sqrt3+i=2e^{i\pi/6}$ y

$$
(\sqrt3+i)^6=2^6e^{i\pi}=\boxed{-64}.
$$

## 4. Interpretación y comprobaciones

- Multiplicar por $re^{i\theta}$ rota $\theta$ y escala por $r$.
- Multiplicar por $i$ rota $\pi/2$ en sentido antihorario sin cambiar el módulo.
- **Control:** para $z=(1+i)$, $|z^2|=|z|^2=2$ y $z^2=2i$ tiene módulo $2$.
- **Caso especial:** $z=0$ tiene módulo, pero no argumento definido.

## 5. En mis palabras

> [!note] Explicación personal
> Explica por qué elevar $z$ a una potencia multiplica su argumento, sin recurrir a una expansión binomial.

## 6. Qué debo poder reconstruir sin consultar

- [ ] Pasar de cartesiana a polar, identificando el cuadrante correcto.
- [ ] Deducir la regla de multiplicación y potencias en forma polar.

## 7. Recuperación activa

1. **Pregunta conceptual:** ¿por qué conocer solamente $\tan\theta=y/x$ no siempre basta para determinar el argumento?
2. **Aplicación breve:** expresa $-1+i\sqrt3$ en forma polar y calcula su cuarta potencia.

## 8. Conexiones y dudas

- **Se relaciona con:** [[Números complejos, operaciones y módulo]], [[Exponencial compleja]], [[Raíces complejas y ramas]], [[Logaritmo complejo y ramas]].
- **Dudas pendientes:** argumentos en el semieje real negativo y diferencias entre convenciones.

## 9. Tarjetas Anki Bridge (solo si aportan valor)

¿Qué hace la multiplicación por $re^{i\theta}$ a un complejo del plano? ⇢%%oab:basic:v1%%Escala su módulo por $r$ y rota su argumento en $\theta$ (módulo $2\pi$).

¿Por qué un número complejo no nulo tiene infinitos argumentos? ⇢%%oab:basic:v1%%Porque $e^{i(\theta+2\pi k)}=e^{i\theta}$ para cualquier $k\in\mathbb Z$.
