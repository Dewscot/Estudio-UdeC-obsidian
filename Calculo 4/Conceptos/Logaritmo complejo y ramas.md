---
tags:
  - concepto
  - calculo-iv
  - funciones-complejas
tipo: concepto
asignatura: "Cálculo IV"
unidad: "Semana 3 — Exponencial, logaritmo, raíces y funciones trigonométricas"
estado: pendiente
fuente: "Apunte del profesor: Exponencial, logaritmo, raíces y funciones trig.pdf"
---

> [!abstract] Pregunta central
> ¿Por qué el logaritmo complejo necesita escoger una rama y cómo afecta esa elección a su dominio, sus propiedades y las integrales de $1/z$?

## 1. Idea e interpretación intuitiva

En $\mathbb{R}_{>0}$, la exponencial es inyectiva y tiene inversa $\ln x$. En $\mathbb{C}$ ocurre algo distinto:

$$
e^{w+2\pi i}=e^w.
$$

Por eso, una misma imagen tiene infinitos antecedentes. **Para obtener una inversa de valor único hay que restringir los argumentos** y excluir un corte del plano. Este problema es geométrico: una vuelta completa alrededor del origen agrega $2\pi$ al ángulo, sin cambiar el número complejo.

## 2. Fundamentos, hipótesis y convenciones

- **Exponencial:** $e^{x+iy}=e^x(\cos y+i\sin y)$; nunca se anula.
- **Representación polar:** si $z\ne0$, $z=re^{i\theta}$, con $r=|z|>0$ y $\theta$ definido módulo $2\pi$.
- **Logaritmo multivaluado:** $\log z=\{\ln r+i(\theta+2\pi k):k\in\mathbb Z\}$, donde $\theta$ representa cualquier argumento fijo de $z$.
- **Convención del apunte:** la rama principal usa $-\pi<\operatorname{Arg}(z)<\pi$ y un corte en el semieje real no positivo; $\operatorname{Log}$ se define en $D=\mathbb C\setminus(-\infty,0]$.
- **Condición:** nunca se define un logaritmo de $0$.

## 3. Desarrollo matemático o procedimiento

**Construcción de la rama principal.** Restringimos $w=x+iy$ a la franja $-\pi<y<\pi$. La aplicación $e^w$ es allí inyectiva y su imagen es $D$. Si $z=re^{i\theta}\in D$, con $-\pi<\theta<\pi$, la inversa queda

$$
\boxed{\operatorname{Log}z=\ln|z|+i\operatorname{Arg}(z)}.
$$

**Derivada.** Como $e^{\operatorname{Log}z}=z$ en $D$, al derivar:

$$
e^{\operatorname{Log}z}(\operatorname{Log}z)'=1
\quad\Longrightarrow\quad
\boxed{(\operatorname{Log}z)'=\frac1z}.
$$

**Productos y ramas.** Los argumentos se suman módulo $2\pi$, por lo que, cuando todas las expresiones están definidas,

$$
\operatorname{Log}(z_1z_2)
=\operatorname{Log}z_1+\operatorname{Log}z_2+2\pi ki,
\quad k\in\mathbb Z.
$$

No es correcto eliminar sin más el término $2\pi ki$.

**Otras ramas.** Se puede escoger $\alpha<\arg z<\alpha+2\pi$ y excluir el rayo correspondiente al corte angular; así surge otra función $\operatorname{Log}_\alpha$.

## 4. Interpretación y comprobaciones

- **Significado:** elegir una rama equivale a seleccionar continuamente un argumento para cada punto del dominio elegido.
- **Condiciones y límites:** $\operatorname{Log}$ no es la inversa de $e^w$ sobre todo $\mathbb C$; depende de la franja y del corte escogidos.
- **Contraejemplo:** si $z_1=z_2=e^{3\pi i/4}$, entonces $\operatorname{Log}(z_1z_2)=-\pi i/2$, pero $\operatorname{Log}z_1+\operatorname{Log}z_2=3\pi i/2$.
- **Relación con integrales:** $\operatorname{Log}$ es una primitiva de $1/z$ en $D$, pero $1/z$ no tiene primitiva en todo $\mathbb C\setminus\{0\}$; ver [[Primitivas complejas e independencia del camino]].

## 5. En mis palabras

> [!note] Explicación personal
> Completar sin consultar: ¿por qué quitar un rayo del plano permite definir un logaritmo de valor único? Ilustrarlo con una vuelta alrededor del origen.

## 6. Qué debo poder reconstruir sin consultar

- [ ] Justificar la no inyectividad de $e^z$ y construir $\operatorname{Log}z$ a partir de una franja.
- [ ] Explicar el corte, derivar $\operatorname{Log}'(z)=1/z$ y detectar errores al usar propiedades de productos.

## 7. Recuperación activa

1. **Pregunta conceptual:** ¿qué cambia y qué no cambia al escoger otra rama del logaritmo?
2. **Deducción breve:** toma $z=e^{3\pi i/4}$ y compara $\operatorname{Log}(z^2)$ con $2\operatorname{Log}z$.

## 8. Conexiones y dudas

- **Se relaciona con:** [[Primitivas complejas e independencia del camino]], [[Integración compleja sobre caminos]] y las raíces complejas de la Semana 3.
- **Dudas pendientes:** anotar cualquier dificultad para distinguir $\log$ multivaluado de una rama $\operatorname{Log}$.

## 9. Tarjetas Anki Bridge (solo si aportan valor)

¿Por qué la exponencial compleja no tiene inversa global de valor único? ⇢%%oab:basic:v1%%Porque $e^{z+2\pi i}=e^z$; se debe restringir a una franja angular para obtener una inversa.

¿Cuál es el dominio de la rama principal $\operatorname{Log}z$ utilizada en los apuntes y por qué? ⇢%%oab:basic:v1%%$\mathbb C\setminus(-\infty,0]$, porque allí el argumento puede elegirse continuamente con $-\pi<\operatorname{Arg}z<\pi$.
