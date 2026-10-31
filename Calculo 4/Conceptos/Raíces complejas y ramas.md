---
tags:
  - concepto
  - calculo-iv
  - funciones-complejas
tipo: concepto
asignatura: "Cálculo IV"
unidad: "Semana 3 — Exponencial, logaritmo, raíces y funciones trigonométricas"
estado: pendiente
fuente: "Apunte del profesor: Exponencial, logaritmo, raíces y funciones trig.pdf, pp. 5-6"
---

> [!abstract] Pregunta central
> ¿Por qué $w^n=z$ tiene varias soluciones y cómo se selecciona una rama de raíz como función?

## 1. Idea e interpretación intuitiva

Elevar un complejo a la potencia $n$ multiplica su ángulo por $n$. Al deshacer esa operación aparecen $n$ ángulos diferentes, que corresponden a $n$ raíces. Una rama escoge sistemáticamente **una** raíz para cada punto de un dominio apropiado.

## 2. Fundamentos, hipótesis y convenciones

- Para $z=re^{i\theta}\neq0$, se buscan $w$ tales que $w^n=z$, con $n\ge2$ entero.
- Los argumentos de $z$ son $\theta+2\pi k$.
- **Rama principal del apunte:** $z^{1/n}=\exp(\operatorname{Log}z/n)$ sobre $\mathbb C\setminus(-\infty,0]$, usando la misma rama principal que [[Logaritmo complejo y ramas]].
- No confundir «todas las soluciones de $w^n=z$» con «el valor de una rama de $z^{1/n}$».

## 3. Desarrollo matemático o procedimiento

Si $w=\rho e^{i\varphi}$, entonces $w^n=\rho^ne^{in\varphi}=re^{i\theta}$ implica

$$
\rho=r^{1/n},\qquad n\varphi=\theta+2\pi k.
$$

De aquí,

$$
\boxed{w_k=r^{1/n}e^{i(\theta+2\pi k)/n}},\quad k=0,\ldots,n-1.
$$

Estas raíces tienen el mismo módulo y argumentos separados por $2\pi/n$.

Si $-\pi<\operatorname{Arg}z<\pi$, la raíz principal es

$$
\boxed{z^{1/n}=\exp\left(\frac{\operatorname{Log}z}{n}\right)=r^{1/n}e^{i\operatorname{Arg}z/n}}.
$$

## 4. Interpretación y comprobaciones

- Las raíces de $1$ son $e^{2\pi ik/n}$; forman un polígono regular sobre la circunferencia unidad.
- **Comprobación:** $(w_k)^n=re^{i(\theta+2\pi k)}=z$.
- **Producto de raíces principales:** en general $(z_1z_2)^{1/n}\neq z_1^{1/n}z_2^{1/n}$; las expresiones pueden diferir en una raíz $n$-ésima de la unidad (cuando todos los términos están definidos).
- **Caso $z=0$:** la ecuación $w^n=0$ tiene solo la solución $w=0$; queda fuera del dominio de la rama principal del apunte.

## 5. En mis palabras

> [!note] Explicación personal
> Explica qué se gana y qué se pierde al sustituir las $n$ raíces posibles por una rama principal de la raíz.

## 6. Qué debo poder reconstruir sin consultar

- [ ] Deducir la expresión de todas las raíces $n$-ésimas.
- [ ] Describir geométricamente su distribución e identificar cuál es la rama principal cuando esté definida.

## 7. Recuperación activa

1. **Pregunta conceptual:** ¿cuántas raíces distintas tiene $z\neq0$ y por qué basta elegir $k=0,\ldots,n-1$?
2. **Problema:** [[Raíces cúbicas de 8i]]; intenta resolverlo antes de consultar la solución.
3. **Comprobación:** toma $z_1=z_2=e^{3\pi i/4}$ y compara las raíces cuadradas principales de $z_1z_2$ y de los factores.

## 8. Conexiones y dudas

- **Se relaciona con:** [[Forma polar, argumento y potencias]], [[Exponencial compleja]], [[Logaritmo complejo y ramas]], [[Raíces cúbicas de 8i]].
- **Dudas pendientes:** elegir ramas sin aplicar inadvertidamente propiedades reales que fallan.

## 9. Tarjetas Anki Bridge (solo si aportan valor)

¿Cuántas raíces $n$-ésimas distintas tiene $z\neq0$? ⇢%%oab:basic:v1%%Exactamente $n$; todas tienen módulo $|z|^{1/n}$ y ángulos separados por $2\pi/n$.

¿Por qué no siempre se puede distribuir una raíz principal sobre un producto? ⇢%%oab:basic:v1%%Porque la suma de argumentos puede salir del intervalo de la rama y requerir un ajuste de $2\pi$.
