---
tags:
  - concepto
  - calculo-iv
  - integracion-compleja
tipo: concepto
asignatura: "Cálculo IV"
unidad: "Semana 6 — Teorema de Cauchy-Goursat"
estado: pendiente
fuente: "Apunte del profesor: Teorema de Cauchy-Goursat.pdf"
---

> [!abstract] Pregunta central
> ¿Cuándo se anula una integral sobre una curva cerrada y cuándo podemos sustituir un contorno complicado por otro más sencillo?

## 1. Idea e interpretación intuitiva

La holomorfía en la región encerrada por una curva permite concluir que la integral cerrada es cero **sin parametrizarla**. Si hay puntos problemáticos en su interior, a veces se puede **deformar el contorno**, siempre que el integrando sea holomorfo en la región que se atraviesa durante la deformación.

## 2. Fundamentos, hipótesis y convenciones

- **Cauchy–Goursat (versión del curso):** para una curva cerrada simple $C$, suave por tramos y orientada positivamente, si $f$ es holomorfa en un abierto que contiene $C$ y su interior, entonces $\oint_Cf(z)dz=0$.
- **Deformación:** para dos curvas cerradas simples anidadas y orientadas antihorariamente, si $f$ es holomorfa en la región entre ambas y sobre sus fronteras, sus integrales son iguales.
- **Puntos problemáticos:** donde el integrando deja de ser holomorfo; antes de aplicar un teorema se debe localizar cuáles están encerrados.
- **Convención:** si se orienta la curva interior como frontera de la región anular, su sentido es horario; al escribir la igualdad entre integrales antihorarias este cambio de signo ya está considerado.

## 3. Desarrollo matemático o procedimiento

**Teorema:**

$$
\boxed{f\text{ holomorfa en y dentro de }C\Longrightarrow\oint_Cf(z)\,dz=0}.
$$

**Idea de demostración del profesor.** Escribiendo $f=u+iv$ y $dz=dx+i\,dy$,

$$
\oint_Cf(z)dz=\oint_C(u\,dx-v\,dy)+i\oint_C(v\,dx+u\,dy).
$$

Con la regularidad $C^1$ requerida para usar directamente Green, las ecuaciones de Cauchy–Riemann $u_x=v_y$ y $u_y=-v_x$ anulan ambas integrales dobles. El enunciado general de Cauchy–Goursat no requiere añadir $C^1$ como hipótesis.

**Deformación:** si $C_{\rm ext}$ y $C_{\rm int}$ encierran una zona anular sin problemas de holomorfía,

$$
\boxed{\oint_{C_{\rm ext}}f(z)dz=\oint_{C_{\rm int}}f(z)dz}
$$

con ambas curvas consideradas antihorarias. Si hay varios puntos aislados problemáticos, la integral exterior puede descomponerse en una suma de pequeñas integrales en torno a ellos, bajo las hipótesis correspondientes.

## 4. Interpretación y comprobaciones

- **Ejemplo con integral nula:** $\oint_{|z|=1}e^z/(z-2)\,dz=0$, porque $z=2$ está fuera del círculo.
- **Ejemplo con deformación:** para una elipse antihoraria que rodea $0$, $\oint_C dz/z=2\pi i$ al deformarla hacia un círculo alrededor del origen.
- **Advertencia:** una singularidad encerrada impide aplicar Cauchy–Goursat directamente, pero **no garantiza** que la integral sea distinta de cero: $\oint_C dz/z^2=0$ cuando $C$ es cerrada y evita $0$, por su primitiva $-1/z$.
- **Error habitual:** comprobar holomorfía solo sobre $C$, olvidando su interior.

## 5. En mis palabras

> [!note] Explicación personal
> Completar: dibuja dos contornos anidados y explica en qué región hay que verificar holomorfía para deformar uno en el otro.

## 6. Qué debo poder reconstruir sin consultar

- [ ] Enunciar Cauchy–Goursat indicando la región relevante.
- [ ] Identificar cuándo la deformación de caminos es válida y cómo interviene la orientación.

## 7. Recuperación activa

1. **Pregunta conceptual:** ¿por qué el hecho de que $1/z$ sea holomorfa sobre $|z|=1$ no permite usar Cauchy–Goursat allí?
2. **Aplicación breve:** un cuadrado antihorario encierra $0$ y no encierra $3$. ¿Qué herramientas permiten evaluar $\oint_C(z\cos z+i/z)dz$?

## 8. Conexiones y dudas

- **Se relaciona con:** [[Integración compleja sobre caminos]], [[Primitivas complejas e independencia del camino]], [[Fórmula integral de Cauchy]].
- **Dudas pendientes:** interpretar deformaciones cuando hay varios agujeros o puntos excepcionales.

## 9. Tarjetas Anki Bridge (solo si aportan valor)

¿Cuál es la condición espacial indispensable para aplicar Cauchy–Goursat a una curva cerrada simple? ⇢%%oab:basic:v1%%Que la función sea holomorfa en un abierto que contenga la curva y todo su interior, no solamente sobre la curva.

¿En qué región debe ser holomorfa una función para deformar una curva cerrada en otra sin cambiar su integral? ⇢%%oab:basic:v1%%En la región barrida entre ambos contornos y sobre sus fronteras; las integrales coinciden si las dos curvas se consideran con la misma orientación positiva.
