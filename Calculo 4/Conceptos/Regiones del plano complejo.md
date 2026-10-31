---
tags:
  - concepto
  - calculo-iv
  - regiones-complejas
tipo: concepto
asignatura: "Cálculo IV"
unidad: "Semana 2 — Regiones de C y funciones complejas"
estado: pendiente
fuente: "Apunte del profesor: Semana 2.pdf, pp. 1-4"
---

> [!abstract] Pregunta central
> ¿Cómo distinguir conjuntos abiertos, cerrados, fronteras y puntos de acumulación en el plano complejo?

## 1. Idea e interpretación intuitiva

En $\mathbb C\simeq\mathbb R^2$, las distancias permiten describir regiones sin recurrir a coordenadas por separado. Una región abierta ofrece un pequeño disco alrededor de cada punto propio; un conjunto cerrado contiene todos sus puntos frontera.

## 2. Fundamentos, hipótesis y convenciones

- **Disco abierto:** $D(z_0;R)=\{z:|z-z_0|<R\}$, con $R>0$.
- **Disco cerrado:** $\overline D(z_0;R)=\{z:|z-z_0|\le R\}$.
- **Abierto:** $A$ es abierto si $\forall z\in A\,\exists\varepsilon>0:D(z;\varepsilon)\subseteq A$.
- **Cerrado:** $B$ es cerrado si $\mathbb C\setminus B$ es abierto.

## 3. Desarrollo matemático o procedimiento

La **frontera** $\operatorname{Fr}(A)$ contiene los puntos donde todo disco intersecta tanto $A$ como su complemento. La **clausura** es

$$
\boxed{\overline A=A\cup\operatorname{Fr}(A)}.
$$

Un punto $z_0$ es de **acumulación** de $A$ si todo disco $D(z_0;\varepsilon)$ contiene un punto de $A$ distinto de $z_0$.

**Ejemplo:** si $A=\{1/n:n\in\mathbb N\}$, entonces $0\notin A$, pero $0$ es punto de acumulación, pues para todo $\varepsilon>0$ puede tomarse $n>1/\varepsilon$.

**Por qué un disco abierto es abierto:** dado $w\in D(z_0;R)$, elegimos $\rho=R-|w-z_0|>0$. Por desigualdad triangular, si $|z-w|<\rho$, entonces $|z-z_0|<R$.

## 4. Interpretación y comprobaciones

- $\operatorname{Fr}(D(z_0;R))=\{z:|z-z_0|=R\}$.
- $\mathbb C\setminus\{0\}$ es abierto; su complemento $\{0\}$ es cerrado.
- $\mathbb C$ y $\varnothing$ son ambos abiertos y cerrados: las categorías no son excluyentes.
- Un punto de acumulación puede **no** pertenecer al conjunto; no debe confundirse con un punto aislado.

## 5. En mis palabras

> [!note] Explicación personal
> Describe con tus palabras qué se debe poder dibujar alrededor de cada punto para verificar que un conjunto sea abierto.

## 6. Qué debo poder reconstruir sin consultar

- [ ] Probar que $D(z_0;R)$ es abierto usando la desigualdad triangular.
- [ ] Distinguir frontera, clausura y puntos de acumulación en ejemplos concretos.

## 7. Recuperación activa

1. **Pregunta conceptual:** ¿un conjunto puede ser simultáneamente abierto y cerrado? Da un ejemplo.
2. **Aplicación breve:** clasifica $\{z:\operatorname{Re}z>0\}$ y calcula su frontera.
3. **Contraejemplo:** ¿por qué $\mathbb C\setminus(0,\infty)$ no es abierto?

## 8. Conexiones y dudas

- **Se relaciona con:** [[Números complejos, operaciones y módulo]], [[Funciones complejas e imágenes de conjuntos]], [[Logaritmo complejo y ramas]].
- **Dudas pendientes:** diferenciar un conjunto cerrado de uno simplemente «no abierto».

## 9. Tarjetas Anki Bridge (solo si aportan valor)

¿Cuál es el criterio para que $A\subseteq\mathbb C$ sea abierto? ⇢%%oab:basic:v1%%Cada $z\in A$ tiene algún disco $D(z;\varepsilon)$ completamente contenido en $A$.

¿Puede un punto de acumulación de $A$ estar fuera de $A$? ⇢%%oab:basic:v1%%Sí; $0$ acumula los puntos de $\{1/n:n\in\mathbb N\}$ y no pertenece al conjunto.
