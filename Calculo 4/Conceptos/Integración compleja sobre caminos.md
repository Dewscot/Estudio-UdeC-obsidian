---
tags:
  - concepto
  - calculo-iv
  - integracion-compleja
tipo: concepto
asignatura: "Cálculo IV"
unidad: "Semana 5 — Integración sobre un camino, primitivas"
estado: pendiente
fuente: "Apunte del profesor: Integración sobre un camino, primitivas.pdf"
---

> [!abstract] Pregunta central
> ¿Cómo se calcula $\int_C f(z)\,dz$ y qué información de un camino importa para que la integral quede bien definida?

## 1. Idea e interpretación intuitiva

En vez de integrar sobre un intervalo real, recorremos una curva del plano complejo. **Parametrizar el camino convierte la integral compleja en una integral ordinaria respecto de un parámetro real.** El sentido de recorrido importa; la rapidez concreta de la parametrización, no.

## 2. Fundamentos, hipótesis y convenciones

- **Camino:** $\gamma:[a,b]\to\mathbb C$, $\gamma(t)=x(t)+iy(t)$, continuo y suave por tramos.
- **Función:** $f$ continua sobre la imagen del camino; no hace falta exigir holomorfía para definir la integral.
- **Extremos:** $z_0=\gamma(a)$ y $z_1=\gamma(b)$.
- **Orientación positiva:** para curvas cerradas simples, antihoraria respecto del interior.
- **Notación:** $\int_C$ para un camino y $\oint_C$ para uno cerrado.

## 3. Desarrollo matemático o procedimiento

La definición es

$$
\boxed{\int_C f(z)\,dz=\int_a^b f(\gamma(t))\gamma'(t)\,dt}.
$$

En la práctica:

1. Identificar los extremos, la forma del contorno y el sentido.
2. Elegir $z=\gamma(t)$ y un intervalo $[a,b]$.
3. Derivar $\gamma'(t)$, sustituir $z$ por $\gamma(t)$ y $dz$ por $\gamma'(t)dt$.
4. Resolver la integral en $t$ (partes real e imaginaria si conviene).

**Ejemplo fundamental.** Para $C:|z|=1$ antihoraria, $\gamma(t)=e^{it}$, $0\le t\le2\pi$. Por tanto,

$$
\oint_C\frac{dz}{z}
=\int_0^{2\pi}\frac{ie^{it}}{e^{it}}\,dt
=i\int_0^{2\pi}dt
=\boxed{2\pi i}.
$$

## 4. Interpretación y comprobaciones

- **Reparametrización:** la integral no cambia si la nueva parametrización conserva orientación y recorre una vez el mismo camino.
- **Inversión del sentido:** $\int_{-C}f(z)dz=-\int_Cf(z)dz$.
- **Concatenación:** si $C=C_1+C_2$ (recorrido sucesivo), $\int_C f=\int_{C_1}f+\int_{C_2}f$.
- **Error habitual:** olvidar el factor $\gamma'(t)$ o usar $[0,2\pi]$ aunque el arco sea solo una parte de la circunferencia.
- **Límite de aplicación:** el resultado $2\pi i$ anterior depende de que el círculo se recorra una vez y antihorariamente.

## 5. En mis palabras

> [!note] Explicación personal
> Completar: ¿qué representa $\gamma'(t)dt$ y por qué cambia el signo al recorrer un camino en sentido contrario?

## 6. Qué debo poder reconstruir sin consultar

- [ ] Parametrizar un segmento, arco y circunferencia con sentido especificado.
- [ ] Deducir la fórmula de la integral y comprobar el resultado de $\oint_{|z|=1}dz/z$.

## 7. Recuperación activa

1. **Pregunta conceptual:** ¿por qué $f$ no necesita ser holomorfa para poder definir $\int_Cf(z)dz$?
2. **Aplicación breve:** parametriza el semicírculo superior de radio $R$, desde $R$ a $-R$, y escribe (sin resolver) $\int_C \bar z\,dz$.

## 8. Conexiones y dudas

- **Se relaciona con:** [[Primitivas complejas e independencia del camino]], [[Teorema de Cauchy-Goursat y deformación]] y [[Fórmula integral de Cauchy]].
- **Dudas pendientes:** documentar problemas de parametrización, orientación o límites de integración.

## 9. Tarjetas Anki Bridge (solo si aportan valor)

¿Qué dos elementos del camino debo fijar al parametrizar una integral compleja y por qué? ⇢%%oab:basic:v1%%La trayectoria y su orientación: la integral es independiente de una reparametrización regular que conserve ambas, pero cambia de signo si invierto el sentido.

¿Para definir $\int_C f(z)\,dz$ es necesario que $f$ sea holomorfa? ⇢%%oab:basic:v1%%No. Basta continuidad de $f$ sobre un camino suave por tramos; la holomorfía se necesita para teoremas adicionales de cálculo de integrales.
