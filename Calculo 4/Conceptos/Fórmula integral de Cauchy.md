---
tags:
  - concepto
  - calculo-iv
  - integracion-compleja
tipo: concepto
asignatura: "Cálculo IV"
unidad: "Semana 8 — Fórmula integral de Cauchy"
estado: pendiente
fuente: "Apunte del profesor: Fórmula integral de Cauchy.pdf"
---

> [!abstract] Pregunta central
> ¿Cómo obtener el valor de una integral cerrada mediante una simple evaluación de una función holomorfa en un punto interior?

## 1. Idea e interpretación intuitiva

Cauchy–Goursat anula integrales de funciones holomorfas. La **fórmula integral de Cauchy** calcula integrales cuyos integrandos contienen el factor $1/(z-z_0)$, aun cuando esa expresión no esté definida en $z_0$.

La información de $f$ sobre el contorno determina su valor en un punto interior.

## 2. Fundamentos, hipótesis y convenciones

- **Contorno:** $C$ cerrado simple, suave por tramos, orientado antihorariamente.
- **Punto:** $z_0$ debe estar estrictamente en el interior de $C$.
- **Función del numerador:** $f$ debe ser holomorfa en un abierto que contenga $C$ y su interior.
- **No confundir:** no se exige que $f(z)/(z-z_0)$ sea holomorfa en el interior; precisamente puede fallar en $z_0$.

## 3. Desarrollo matemático o procedimiento

$$
\boxed{f(z_0)=\frac{1}{2\pi i}\oint_C\frac{f(z)}{z-z_0}\,dz}
\qquad\Longleftrightarrow\qquad
\boxed{\oint_C\frac{f(z)}{z-z_0}\,dz=2\pi i f(z_0)}.
$$

**Por qué funciona (idea del apunte).** Separamos $f(z)=f(z_0)+[f(z)-f(z_0)]$:

$$
\oint_C\frac{f(z)}{z-z_0}dz=
 f(z_0)\oint_C\frac{dz}{z-z_0}+
 \oint_C\frac{f(z)-f(z_0)}{z-z_0}dz.
$$

La primera integral vale $2\pi i f(z_0)$. Por deformación se reduce la segunda a un círculo pequeño de radio $\varepsilon$ alrededor de $z_0$; como el cociente tiende a $f'(z_0)$ y la longitud es $2\pi\varepsilon$, esa integral tiende a cero.

**Ejemplo:** si $C:|z|=1$ es antihoraria,

$$
\oint_C\frac{e^z}{z}dz=2\pi i\,e^0=\boxed{2\pi i}.
$$

## 4. Interpretación y comprobaciones

- **Reconocimiento:** reescribir el integrando en la forma $f(z)/(z-z_0)$; verificar que el resto $f$ sea holomorfo en la región relevante.
- **Ejemplo con factores:** sobre $|z-1|=1$, $\cos(iz)/[(z-1)(z+2)]$ corresponde a $z_0=1$ y $f(z)=\cos(iz)/(z+2)$, de donde su integral es $2\pi i\cos(i)/3$.
- **Signo:** si $C$ se recorre en sentido horario, el resultado cambia de signo.
- **Contraejemplo de aplicación:** si $z_0$ está fuera de la curva, no se aplica esta versión interior de la fórmula.
- **Varios puntos problemáticos:** se puede combinar con la deformación de contornos, separando aportes (como en los ejemplos del profesor).

## 5. En mis palabras

> [!note] Explicación personal
> Completar: ¿qué es lo que debe ser holomorfo: el integrando completo o la función $f$ que se identifica al separar $z-z_0$?

## 6. Qué debo poder reconstruir sin consultar

- [ ] Enunciar las hipótesis precisas de la fórmula integral de Cauchy.
- [ ] Separar $f(z)/(z-z_0)$ y justificar el argumento del círculo pequeño.

## 7. Recuperación activa

1. **Pregunta conceptual:** ¿por qué la singularidad aparente del factor $1/(z-z_0)$ no contradice la aplicación de la fórmula?
2. **Aplicación breve:** en $C:|z-1|=1$, decide si puedes aplicar la fórmula a $\cos(iz)/[(z-1)(z+2)]$ e identifica $f(z)$ y $z_0$ antes de calcular.

## 8. Conexiones y dudas

- **Se relaciona con:** [[Teorema de Cauchy-Goursat y deformación]], [[Primitivas complejas e independencia del camino]], [[Fórmula integral generalizada y desigualdad de Cauchy]].
- **Dudas pendientes:** cuándo separar contornos y cuándo basta una sola evaluación.

## 9. Tarjetas Anki Bridge (solo si aportan valor)

¿Qué condiciones permiten aplicar $\oint_C f(z)/(z-z_0)\,dz=2\pi i f(z_0)$? ⇢%%oab:basic:v1%%$C$ es cerrada simple y antihoraria, $z_0$ está en su interior y $f$ es holomorfa en un abierto que contiene la curva y todo su interior.

¿Cuál es el error al exigir que todo el integrando $f(z)/(z-z_0)$ sea holomorfo dentro del contorno antes de aplicar la fórmula integral de Cauchy? ⇢%%oab:basic:v1%%La condición se aplica al numerador $f$, no al cociente completo; este puede ser no holomorfo en $z_0$ y aun así ser exactamente el caso previsto por la fórmula.
