---
tags:
  - concepto
  - calculo-iv
  - funciones-complejas
tipo: concepto
asignatura: "Cálculo IV"
unidad: "Semana 3 — Exponencial, logaritmo, raíces y funciones trigonométricas"
estado: pendiente
fuente: "Apunte del profesor: Exponencial, logaritmo, raíces y funciones trig.pdf, pp. 7-10"
---

> [!abstract] Pregunta central
> ¿Cómo se definen seno y coseno en $\mathbb C$ y qué cambia con respecto al caso real?

## 1. Idea e interpretación intuitiva

Las identidades de Euler permiten definir seno y coseno usando la exponencial compleja. Conservan sus identidades algebraicas y periodicidad, pero su módulo **ya no está acotado por $1$** al permitir entradas con parte imaginaria.

## 2. Fundamentos, hipótesis y convenciones

- Las definiciones valen para cualquier $z\in\mathbb C$.
- **Funciones hiperbólicas:** $\cosh y=(e^y+e^{-y})/2$ y $\sinh y=(e^y-e^{-y})/2$.
- **Funciones cociente:** $\tan z=\sin z/\cos z$ y $\cot z=\cos z/\sin z$ solo donde el denominador no se anula.

## 3. Desarrollo matemático o procedimiento

A partir de $e^{iz}$ y $e^{-iz}$ se define

$$
\boxed{\cos z=\frac{e^{iz}+e^{-iz}}{2}},\qquad
\boxed{\sin z=\frac{e^{iz}-e^{-iz}}{2i}}.
$$

Con $z=x+iy$, usando las fórmulas de suma se obtiene

$$
\cos(x+iy)=\cos x\cosh y-i\sin x\sinh y,
$$

$$
\sin(x+iy)=\sin x\cosh y+i\cos x\sinh y.
$$

En particular,

$$
\boxed{\cos(iy)=\cosh y},\qquad
\boxed{\sin(iy)=i\sinh y}.
$$

Para una recta vertical $x=a$, si $w=\alpha+i\beta=\cos(a+iy)$ y $\sin a\cos a\neq0$, entonces

$$
\frac{\alpha^2}{\cos^2a}-\frac{\beta^2}{\sin^2a}=1,
$$

una hipérbola; el apunte analiza esta imagen geométrica.

## 4. Interpretación y comprobaciones

- **No acotación:** $\cosh y\to\infty$ cuando $|y|\to\infty$, de modo que $\cos z$ no está acotado en $\mathbb C$.
- **Identidades:** $\cos^2z+\sin^2z=1$ y $\sin(z+2\pi)=\sin z$.
- **Ceros:** $\sin z=0\iff z=k\pi$; $\cos z=0\iff z=\pi/2+k\pi$, con $k\in\mathbb Z$.
- **Dominios:** excluir $\pi/2+k\pi$ para $\tan$ y $k\pi$ para $\cot$.
- **Caso especial:** para $a=0$, la imagen de $\cos(iy)$ es el rayo real $[1,\infty)$, no una hipérbola no degenerada.

## 5. En mis palabras

> [!note] Explicación personal
> Explica por qué $\cos x$ está acotado en $\mathbb R$ pero $\cos(x+iy)$ no necesariamente lo está.

## 6. Qué debo poder reconstruir sin consultar

- [ ] Obtener las definiciones exponenciales de $\sin z$ y $\cos z$.
- [ ] Calcular $\cos(x+iy)$ y reconocer las funciones hiperbólicas.
- [ ] Determinar los puntos excluidos en los dominios de $\tan z$ y $\cot z$.

## 7. Recuperación activa

1. **Pregunta conceptual:** ¿por qué las identidades trigonométricas siguen siendo válidas en $\mathbb C$?
2. **Deducción breve:** demuestra que $\cos(iy)=\cosh y$ a partir de la definición exponencial.
3. **Aplicación geométrica:** ¿qué imagen tiene la recta $x=\pi/2$ bajo $\cos z$?

## 8. Conexiones y dudas

- **Se relaciona con:** [[Exponencial compleja]], [[Funciones complejas e imágenes de conjuntos]], [[Logaritmo complejo y ramas]].
- **Dudas pendientes:** recordar qué resultados reales cambian cuando la variable puede tener parte imaginaria.

## 9. Tarjetas Anki Bridge (solo si aportan valor)

¿Por qué $\cos z$ no es una función acotada en $\mathbb C$? ⇢%%oab:basic:v1%%Porque $\cos(iy)=\cosh y$, y $\cosh y$ crece sin cota cuando $|y|\to\infty$.

¿Dónde se anula $\cos z$ para $z\in\mathbb C$? ⇢%%oab:basic:v1%%Solo en los valores reales $z=\pi/2+k\pi$, con $k\in\mathbb Z$.
