---
tags:
  - concepto
  - calculo-iv
  - funciones-complejas
tipo: concepto
asignatura: "Cálculo IV"
unidad: "Semana 2 — Regiones de C y funciones complejas"
estado: pendiente
fuente: "Apunte del profesor: Semana 2.pdf, pp. 5-11"
---

> [!abstract] Pregunta central
> ¿Cómo visualizar una función $f:\mathbb C\to\mathbb C$ y estudiar la imagen geométrica de un conjunto?

## 1. Idea e interpretación intuitiva

Una función compleja transforma puntos de un plano en puntos de otro. Su gráfica completa vive en cuatro dimensiones, pero podemos estudiar sus componentes reales o la transformación de conjuntos sencillos (rectas, circunferencias, discos).

## 2. Fundamentos, hipótesis y convenciones

- **Dominio e imagen:** $f:A\subseteq\mathbb C\to\mathbb C$ y $f(B)=\{f(z):z\in B\}$ para $B\subseteq A$.
- **Descomposición:** $z=x+iy$, $w=f(z)=u(x,y)+iv(x,y)$.
- **Visualización:** $u$, $v$ y $|f|$ son funciones reales de dos variables; no representan por separado toda la gráfica de $f$.
- Para $f(z)=1/z$, excluir siempre $z=0$.

## 3. Desarrollo matemático o procedimiento

**Ejemplo 1, $f(z)=z^2$.**

$$
(x+iy)^2=(x^2-y^2)+i(2xy),
$$

por lo que $u=x^2-y^2$, $v=2xy$ y $|f(z)|=x^2+y^2$.

En polares,

$$
z=re^{i\theta}\quad\Longrightarrow\quad z^2=r^2e^{2i\theta}.
$$

**Imagen de una recta vertical:** si $x=a\neq0$ y $w=\alpha+i\beta=z^2$, entonces

$$
\alpha=a^2-y^2,\quad\beta=2ay
\quad\Longrightarrow\quad
\boxed{\alpha=a^2-\frac{\beta^2}{4a^2}},
$$

una parábola en el plano $w$.

**Ejemplo 2, $f(z)=1/z$.**

$$
w=\frac{x-iy}{x^2+y^2},\qquad
z=re^{i\theta}\Longrightarrow w=r^{-1}e^{-i\theta}.
$$

Para una recta $\operatorname{Re}z=a\neq0$, su imagen es una circunferencia de centro $1/(2a)$ y radio $1/(2|a|)$, **sin el origen**.

## 4. Interpretación y comprobaciones

- $z^2$ transforma $r\mapsto r^2$ y $\theta\mapsto2\theta$.
- $1/z$ transforma $r\mapsto 1/r$ y $\theta\mapsto-\theta$.
- El origen no puede pertenecer a la imagen de $1/z$, porque $1/z\neq0$.
- **Caso degenerado:** la imagen de la recta $x=0$ bajo $z^2$ no es una parábola no degenerada; es el semieje real no positivo.
- **Comprobación:** $|z-i|=1$, excluyendo $z=0$, se transforma bajo $1/z$ en la recta $\operatorname{Im}w=-1/2$.

## 5. En mis palabras

> [!note] Explicación personal
> Explica por qué estudiar $f(A)$ informa sobre una función compleja aunque su gráfica total no pueda dibujarse en $\mathbb R^3$.

## 6. Qué debo poder reconstruir sin consultar

- [ ] Separar una función en componentes $u(x,y)$ y $v(x,y)$.
- [ ] Eliminar el parámetro para hallar la imagen de una recta bajo $z^2$.
- [ ] Interpretar la transformación $z\mapsto1/z$ en polares.

## 7. Recuperación activa

1. **Pregunta conceptual:** ¿por qué $f:\mathbb C\to\mathbb C$ requiere cuatro coordenadas reales para su gráfica?
2. **Deducción breve:** demuestra que $z^2$ transforma $x=a\neq0$ en una parábola.
3. **Problema:** [[Imagen de una recta vertical bajo la inversión]].

## 8. Conexiones y dudas

- **Se relaciona con:** [[Regiones del plano complejo]], [[Forma polar, argumento y potencias]], [[Exponencial compleja]], [[Imagen de una recta vertical bajo la inversión]].
- **Dudas pendientes:** diferenciar la imagen del conjunto original de la gráfica de la función.

## 9. Tarjetas Anki Bridge (solo si aportan valor)

¿Qué son $u(x,y)$ y $v(x,y)$ si $f(x+iy)=u+iv$? ⇢%%oab:basic:v1%%Son las partes real e imaginaria de la imagen de $x+iy$, ambas funciones reales de dos variables.

¿Qué efecto tiene $z\mapsto1/z$ sobre módulo y argumento, con $z\neq0$? ⇢%%oab:basic:v1%%El módulo pasa de $r$ a $1/r$ y el argumento de $\theta$ a $-\theta$.
