---
tags:
  - concepto
  - calculo-iv
  - integracion-compleja
tipo: concepto
asignatura: "Cálculo IV"
unidad: "Semana 8 — Fórmula generalizada y desigualdad de Cauchy"
estado: pendiente
fuente: "Apuntes del profesor: Fórmula integral de Cauchy.pdf; Fórmula generalizada de Cauchy y desigualdad de Cauchy.pdf"
---

> [!abstract] Pregunta central
> ¿Cómo calcular integrales con potencias superiores de $z-z_0$ y cómo usar esas mismas fórmulas para acotar derivadas complejas?

## 1. Idea e interpretación intuitiva

La fórmula integral de Cauchy no sirve solo para recuperar $f(z_0)$. Si el denominador tiene potencia $n+1$, aparece la **derivada de orden $n$**. La misma representación integral permite estimar cuánto puede crecer una derivada, usando el valor máximo de la función en una circunferencia.

## 2. Fundamentos, hipótesis y convenciones

- **Fórmula generalizada:** $f$ holomorfa en un abierto que contiene $C$ y su interior, $C$ cerrada simple, suave por tramos, orientada antihorariamente, $z_0$ interior y $n\in\{0,1,2,\ldots\}$.
- **Desigualdad:** $f$ holomorfa en una vecindad del disco cerrado $\overline D(z_0;R)$, con $R>0$.
- **Máximo:** $M_R=\max_{|z-z_0|=R}|f(z)|$, que existe por continuidad sobre la circunferencia compacta.

## 3. Desarrollo matemático o procedimiento

**Fórmula integral generalizada:**

$$
\boxed{\oint_C\frac{f(z)}{(z-z_0)^{n+1}}dz
=\frac{2\pi i}{n!}f^{(n)}(z_0)}.
$$

El caso $n=0$ recupera [[Fórmula integral de Cauchy]]. La potencia $1$ pide el valor de la función; la potencia $2$, su primera derivada; la potencia $3$, su segunda derivada, etc.

**Ejemplo del apunte:** $C:|z|=2$ antihoraria,

$$
\oint_C\frac{e^{z^2}}{(z-i)^3}dz
=\frac{2\pi i}{2!}f''(i),\quad f(z)=e^{z^2}.
$$

Como $f''(z)=(2+4z^2)e^{z^2}$, se obtiene $f''(i)=-2/e$ y

$$
\boxed{\oint_C\frac{e^{z^2}}{(z-i)^3}dz=-\frac{2\pi i}{e}}.
$$

**Desigualdad de Cauchy.** Aplicando la estimación de integrales $|\int_Cg(z)dz|\le M\,L(C)$ sobre $|z-z_0|=R$ (de longitud $2\pi R$),

$$
|f^{(n)}(z_0)|
\le\frac{n!}{2\pi}\frac{M_R}{R^{n+1}}(2\pi R)
=\boxed{\frac{n!\,M_R}{R^n}}.
$$

## 4. Interpretación y comprobaciones

- **Elección de $n$:** si el denominador es $(z-z_0)^m$, utilizar $n=m-1$; no olvidar $n!$.
- **El integrando puede dar cero:** tener un factor $(z-z_0)^{-2}$ no obliga a una integral no nula; puede ocurrir que $f'(z_0)=0$.
- **Estimaciones:** $M_R$ es el máximo del **módulo** de $f$ en la circunferencia, no el valor de $f(z_0)$.
- **Restricción:** no elegir un radio que encierre puntos donde $f$ no es holomorfa; comprobar que el disco cerrado está dentro de la región donde se aplica la fórmula.

## 5. En mis palabras

> [!note] Explicación personal
> Completar: explica por qué la potencia $n+1$ del denominador produce la derivada de orden $n$, y por qué en la cota aparece $R^{-n}$.

## 6. Qué debo poder reconstruir sin consultar

- [ ] Aplicar la fórmula generalizada a integrales de segundo y tercer orden, verificando todas las hipótesis.
- [ ] Deducir la desigualdad de Cauchy a partir de la fórmula generalizada y la cota longitud por máximo.

## 7. Recuperación activa

1. **Pregunta conceptual:** ¿cuál es el paso que permite pasar de la fórmula generalizada a la desigualdad de Cauchy?
2. **Aplicación breve:** si $f$ es holomorfa en una vecindad de $\overline D(0;2)$ y $|f(z)|\le5$ en $|z|=2$, encuentra una cota para $|f''(0)|$.

## 8. Conexiones y dudas

- **Se relaciona con:** [[Fórmula integral de Cauchy]], [[Teorema de Cauchy-Goursat y deformación]] y las derivadas complejas (Semana 4).
- **Dudas pendientes:** cuándo conviene usar la fórmula exacta y cuándo solo una estimación.

## 9. Tarjetas Anki Bridge (solo si aportan valor)

En la fórmula integral generalizada de Cauchy, ¿qué derivada aparece cuando el denominador es $(z-z_0)^{n+1}$? ⇢%%oab:basic:v1%%Aparece $f^{(n)}(z_0)$ y el factor de la integral es $2\pi i/n!$, con $f$ holomorfa en y dentro del contorno positivo.

¿Qué información se necesita para usar $|f^{(n)}(z_0)|\le n!M_R/R^n$? ⇢%%oab:basic:v1%%Un disco cerrado de radio $R$ alrededor de $z_0$ donde $f$ sea holomorfa en una vecindad y una cota $M_R$ del módulo $|f|$ sobre su circunferencia.
