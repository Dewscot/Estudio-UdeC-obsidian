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
> ¿Cuándo una integral compleja puede calcularse exclusivamente con los extremos y por qué $1/z$ constituye una excepción importante?

## 1. Idea e interpretación intuitiva

Una **primitiva** convierte una integral sobre un camino en una diferencia entre sus extremos. Esto evita parametrizar, pero la existencia de primitivas depende tanto de la función como del dominio en que se trabaja.

## 2. Fundamentos, hipótesis y convenciones

- **Dominio:** un abierto $D\subseteq\mathbb C$ que contiene el camino.
- **Primitiva:** $F:D\to\mathbb C$ holomorfa con $F'(z)=f(z)$ para todo $z\in D$.
- **Camino:** $C$ suave por tramos y contenido en $D$, desde $z_0$ hasta $z_1$.
- **No confundir:** que $f$ sea holomorfa localmente no basta por sí solo para afirmar que posee primitiva en un dominio con agujeros.

## 3. Desarrollo matemático o procedimiento

Sea $\gamma:[a,b]\to D$ una parametrización. Usamos la regla de la cadena:

$$
\frac{d}{dt}F(\gamma(t))=F'(\gamma(t))\gamma'(t)=f(\gamma(t))\gamma'(t).
$$

Integrando,

$$
\int_C f(z)dz=\int_a^b\frac{d}{dt}F(\gamma(t))dt
=\boxed{F(z_1)-F(z_0)}.
$$

Si $C$ es cerrado, $z_0=z_1$ y

$$
\boxed{\oint_C f(z)\,dz=0}.
$$

**Ejemplo:** $f(z)=1/z^2$ posee primitiva $F(z)=-1/z$ en $\mathbb C\setminus\{0\}$. Por ello su integral sobre cualquier camino cerrado contenido allí es cero.

## 4. Interpretación y comprobaciones

- **Independencia del camino:** dos caminos con los mismos extremos, contenidos en $D$, dan igual integral cuando $f$ tiene primitiva en $D$.
- **Contraejemplo fundamental:** $1/z$ es holomorfa en $\mathbb C\setminus\{0\}$, pero $\oint_{|z|=1}dz/z=2\pi i\neq0$; por tanto no tiene primitiva en todo ese dominio.
- **Importancia del dominio:** en $\mathbb C\setminus(-\infty,0]$, la rama principal $\operatorname{Log}z$ sí es una primitiva de $1/z$.
- **Error habitual:** afirmar que $\oint_C f=0$ solo porque $f$ es holomorfa sobre la curva. Hay que comprobar hipótesis sobre el dominio.

## 5. En mis palabras

> [!note] Explicación personal
> Completar: explica por qué la integral de $1/z$ alrededor del origen impide definir una primitiva global en el plano perforado.

## 6. Qué debo poder reconstruir sin consultar

- [ ] Deducir $\int_C f=F(z_1)-F(z_0)$ mediante la regla de la cadena.
- [ ] Contrastar $1/z$ y $1/z^2$ y explicar el papel del corte del logaritmo.

## 7. Recuperación activa

1. **Pregunta conceptual:** si $\oint_C f\ne0$ para una curva cerrada de $D$, ¿qué concluyes sobre la existencia de una primitiva global en $D$?
2. **Aplicación breve:** encuentra una primitiva de $f(z)=3z^2$ y calcula $\int_Cf(z)dz$ entre $z_0=0$ y $z_1=1+i$, sin parametrizar.

## 8. Conexiones y dudas

- **Se relaciona con:** [[Logaritmo complejo y ramas]], [[Integración compleja sobre caminos]] y [[Teorema de Cauchy-Goursat y deformación]].
- **Dudas pendientes:** distinguir primitiva local, primitiva en un dominio y holomorfía.

## 9. Tarjetas Anki Bridge (solo si aportan valor)

¿Qué implica para una integral sobre un camino que $f$ posea una primitiva $F$ en un dominio que contiene ese camino? ⇢%%oab:basic:v1%%Depende solo de los extremos: $\int_C f(z)dz=F(z_1)-F(z_0)$; en particular, si el camino es cerrado, la integral vale cero.

¿Por qué $1/z$ no tiene primitiva global en $\mathbb C\setminus\{0\}$, aunque sea holomorfa allí? ⇢%%oab:basic:v1%%Porque $\oint_{|z|=1}dz/z=2\pi i\neq0$; la existencia de una primitiva global obligaría a que toda integral cerrada fuese cero.
