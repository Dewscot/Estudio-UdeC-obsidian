---
tags:
  - concepto
  - calculo-iv
  - funciones-complejas
tipo: concepto
asignatura: "Cálculo IV"
unidad: "Semana 3 — Exponencial, logaritmo, raíces y funciones trigonométricas"
estado: pendiente
fuente: "Apunte del profesor: Exponencial, logaritmo, raíces y funciones trig.pdf, pp. 1-3"
---

> [!abstract] Pregunta central
> ¿Cómo se interpreta geométricamente $e^z$ y por qué su periodicidad obliga a restringir el dominio para invertirla?

## 1. Idea e interpretación intuitiva

La exponencial compleja separa la información de $z=x+iy$: su parte real controla el tamaño de la imagen y su parte imaginaria controla la dirección angular. Como la dirección se repite cada vuelta completa, la exponencial no es inyectiva en todo $\mathbb C$.

## 2. Fundamentos, hipótesis y convenciones

- **Definición:** $e^{x+iy}=e^x(\cos y+i\sin y)$.
- **Dominio:** todo $\mathbb C$; **imagen:** $\mathbb C\setminus\{0\}$.
- **Propiedades:** $e^{z+w}=e^ze^w$, $e^z\neq0$ y $e^{z+2\pi i}=e^z$.
- La función inversa de valor único requiere restringir la exponencial a una franja de anchura $2\pi$ (con extremos excluidos).

## 3. Desarrollo matemático o procedimiento

Para $z=x+iy$,

$$
e^z=e^xe^{iy}=e^x(\cos y+i\sin y).
$$

Como $|e^{iy}|=1$,

$$
\boxed{|e^{x+iy}|=e^x},\qquad
\arg(e^{x+iy})=y\pmod {2\pi}.
$$

Por otra parte, $e^{i(y+2\pi)}=e^{iy}$; de aquí se obtiene

$$
e^{z+2\pi i}=e^z.
$$

En la franja $S=\{x+iy:-\pi<y<\pi\}$, la exponencial es inyectiva y lleva $S$ a $\mathbb C\setminus(-\infty,0]$. Allí admite la inversa estudiada en [[Logaritmo complejo y ramas]].

**Otra transformación del apunte:** $f(z)=iz+1$ corresponde a una rotación de $\pi/2$ seguida de una traslación de $1$.

## 4. Interpretación y comprobaciones

- La recta vertical $x=a$, con $y\in\mathbb R$, se transforma en la circunferencia $|w|=e^a$.
- La recta horizontal $y=b$, con $x\in\mathbb R$, se transforma en el rayo $\{re^{ib}:r>0\}$, sin su extremo en el origen.
- **Comprobación:** $e^{i\pi}=e^{i3\pi}=-1$; dos preimágenes distintas muestran la periodicidad.
- **Advertencia:** la exponencial nunca vale $0$, aunque $e^x\to0$ cuando $x\to-\infty$.

## 5. En mis palabras

> [!note] Explicación personal
> Explica por qué $e^z$ transforma rectas verticales en circunferencias y por qué dos puntos separados por $2\pi i$ tienen la misma imagen.

## 6. Qué debo poder reconstruir sin consultar

- [ ] Obtener el módulo y argumento de $e^{x+iy}$.
- [ ] Justificar la periodicidad y describir la franja donde existe una inversa.

## 7. Recuperación activa

1. **Pregunta conceptual:** ¿qué conjunto es la imagen de $\{z:\operatorname{Re}z=\ln2\}$ bajo $e^z$?
2. **Deducción breve:** determina la imagen de la franja $-\pi<\operatorname{Im}z<\pi$ sin copiar la respuesta.

## 8. Conexiones y dudas

- **Se relaciona con:** [[Forma polar, argumento y potencias]], [[Logaritmo complejo y ramas]], [[Funciones trigonométricas complejas]].
- **Dudas pendientes:** diferencia entre ser periódica y ser inyectiva en un dominio restringido.

## 9. Tarjetas Anki Bridge (solo si aportan valor)

¿Qué controlan $\operatorname{Re}z$ e $\operatorname{Im}z$ en $e^z$? ⇢%%oab:basic:v1%%La parte real fija el módulo $e^{\operatorname{Re}z}$ y la imaginaria fija el argumento módulo $2\pi$.

¿Por qué $e^z$ no puede valer cero para ningún $z\in\mathbb C$? ⇢%%oab:basic:v1%%Porque $|e^z|=e^{\operatorname{Re}z}>0$ para toda parte real finita.
