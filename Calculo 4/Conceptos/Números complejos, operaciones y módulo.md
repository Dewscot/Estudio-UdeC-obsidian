---
tags:
  - concepto
  - calculo-iv
  - numeros-complejos
tipo: concepto
asignatura: "Cálculo IV"
unidad: "Semana 1 — Números complejos"
estado: pendiente
fuente: "Apunte del profesor: Semana1-1.pdf, pp. 1-8"
---

> [!abstract] Pregunta central
> ¿Qué es un número complejo, cómo se opera con él y qué significado geométrico tienen su módulo y su conjugado?

## 1. Idea e interpretación intuitiva

Un número complejo $z=x+iy$ combina dos coordenadas reales en un único objeto. Puede interpretarse como un número al que se aplican operaciones algebraicas y como un punto $(x,y)$ en el plano. La suma desplaza vectores; el módulo mide distancias y el conjugado refleja respecto del eje real.

## 2. Fundamentos, hipótesis y convenciones

- **Definición:** $\mathbb C=\{x+iy:x,y\in\mathbb R,\ i^2=-1\}$, con $\operatorname{Re}z=x$ y $\operatorname{Im}z=y$.
- **Igualdad:** $z_1=z_2$ si y solo si coinciden sus partes real e imaginaria.
- **Notación:** $\bar z=x-iy$ y $|z|=\sqrt{x^2+y^2}\ge0$.
- **Restricción:** el inverso $1/z$ está definido únicamente para $z\neq0$.

## 3. Desarrollo matemático o procedimiento

Sean $z_1=x_1+iy_1$ y $z_2=x_2+iy_2$. Entonces

$$
z_1+z_2=(x_1+x_2)+i(y_1+y_2),
$$

$$
z_1z_2=(x_1x_2-y_1y_2)+i(x_1y_2+y_1x_2),
$$

porque se distribuye el producto y se sustituye $i^2=-1$.

El conjugado permite hallar el inverso:

$$
z\bar z=(x+iy)(x-iy)=x^2+y^2=|z|^2.
$$

Para $z\neq0$,

$$
\boxed{\frac1z=\frac{\bar z}{|z|^2}=\frac{x-iy}{x^2+y^2}}.
$$

Por tanto, para dividir $z_1/z_2$ se multiplica numerador y denominador por $\bar z_2$.

## 4. Interpretación y comprobaciones

- **Distancia:** $|z_1-z_2|$ es la distancia euclidiana entre dos puntos del plano.
- **Circunferencia:** $|z-z_0|=R$; **disco cerrado:** $|z-z_0|\le R$.
- **Propiedades:** $|z_1z_2|=|z_1||z_2|$ y $|z_1+z_2|\le|z_1|+|z_2|$.
- **Comprobación:** si $z=2+i$, entonces $\bar z=2-i$, $|z|=\sqrt5$ y $z^{-1}=(2-i)/5$. Verifica que $zz^{-1}=1$.
- **Advertencia:** $\operatorname{Im}z$ es un número real; no es $iy$.

## 5. En mis palabras

> [!note] Explicación personal
> Explica sin consultar por qué $z\bar z$ siempre es real no negativo y por qué dividir por un complejo se reduce a utilizar su conjugado.

## 6. Qué debo poder reconstruir sin consultar

- [ ] Deducir el producto de dos complejos a partir de $i^2=-1$.
- [ ] Obtener $1/z$ usando $z\bar z=|z|^2$.
- [ ] Interpretar geométricamente $|z_1-z_2|$ y la conjugación.

## 7. Recuperación activa

1. **Pregunta conceptual:** ¿qué diferencia hay entre reflejar un complejo (conjugación) y obtener su inverso?
2. **Aplicación breve:** calcula $(1+2i)/(2-i)$ y comprueba el resultado multiplicándolo por $(2-i)$.
3. **Transferencia geométrica:** describe el conjunto $|z-(3-i)|\le2$ sin dibujarlo primero.

## 8. Conexiones y dudas

- **Se relaciona con:** [[Forma polar, argumento y potencias]], [[Regiones del plano complejo]], [[Funciones complejas e imágenes de conjuntos]].
- **Dudas pendientes:** distinguir producto complejo de producto componente a componente; revisar signos de $i^2$.

## 9. Tarjetas Anki Bridge (solo si aportan valor)

¿Qué representa geométricamente $|z_1-z_2|$ en $\mathbb C$? ⇢%%oab:basic:v1%%La distancia euclidiana entre los puntos $z_1$ y $z_2$ del plano complejo.

¿Cómo se obtiene el inverso de $z\neq0$ a partir del conjugado? ⇢%%oab:basic:v1%%$1/z=\bar z/|z|^2$, porque $z\bar z=|z|^2$.
