---
tags:
  - electromagnetismo-ii
  - ondas
  - ondas-armonicas
aliases:
  - Periodo frecuencia y numero de onda
tipo: concepto
asignatura: "Electromagnetismo II"
---

# Magnitudes fundamentales de las ondas

> [!abstract] Pregunta guía
> ¿Cómo describimos una oscilación que se repite tanto en el tiempo como en el espacio? ¿Por qué el número de onda angular $k$ contiene $2\pi$?

**Curso:** Electromagnetismo II — Unidad de ondas electromagnéticas.  
**Alcance:** conceptos generales de ondas armónicas. La propagación electromagnética en el vacío y las relaciones entre $\vec E$ y $\vec B$ se estudiarán en otra sección.  
**Referencia principal:** presentación del profesor, *Contenido 6 510238 ondas EM*, sección de ondas armónicas y períodos espacial y temporal.

## 1. Una misma oscilación, dos formas de observarla

Una onda armónica que viaja en la dirección $+z$ se puede describir mediante

$$
\boxed{u(z,t)=A\cos(kz-\omega t+\varphi)}.
$$

Aquí $u$ representa la magnitud que oscila y $A$ su amplitud. Para una componente del campo eléctrico, por ejemplo, $u=E$ y $A=E_0$.

La **fase** es el argumento del coseno:

$$
\theta(z,t)=kz-\omega t+\varphi.
$$

Una variación de fase de $2\pi\,\mathrm{rad}$ corresponde a un ciclo completo de la función sinusoidal. **No significa que el campo o la onda deban girar físicamente en un círculo.**

- **En una posición fija** ($z$ constante), observamos cómo oscila la magnitud al transcurrir el tiempo: estudiamos $T$, $f$ y $\omega$.
- **En un instante fijo** ($t$ constante), observamos cómo cambia la magnitud de un punto a otro del espacio: estudiamos $\lambda$ y $k$.

El signo $kz-\omega t$ corresponde a propagación en $+z$ cuando $k,\omega>0$. Con $kz+\omega t$, la propagación sería hacia $-z$.

## 2. Magnitudes temporales

### Período $T$

Tiempo que tarda una oscilación completa **en un punto fijo**. Su unidad es el segundo ($\mathrm s$).

### Frecuencia $f$

Número de ciclos completos que ocurren por unidad de tiempo:

$$
\boxed{f=\frac{1}{T}}, \qquad [f]=\mathrm{Hz}=\mathrm{s}^{-1}.
$$

Ejemplo: ocho ciclos en dos segundos significan $f=8/2=4\,\mathrm{Hz}$; cada ciclo tarda $T=2/8=0.25\,\mathrm s$.

### Frecuencia angular $\omega$

Mide **cuántos radianes de fase cambian por segundo**, no cuántos ciclos ocurren por segundo.

En un período, la fase cambia $2\pi$ radianes; por eso:

$$
\boxed{\omega=\frac{2\pi}{T}=2\pi f},\qquad [\omega]=\mathrm{rad/s}.
$$

## 3. Magnitudes espaciales

### Longitud de onda $\lambda$

Distancia entre puntos consecutivos que se encuentran en la **misma fase** (por ejemplo, entre dos crestas consecutivas) en un instante dado. Su unidad es el metro ($\mathrm m$).

### Número de onda angular $k$: ¿de dónde viene?

En inglés se llama **angular wavenumber**. Describe **cuántos radianes de fase cambian por metro**, no la cantidad total de ondas de un problema.

Congelamos el tiempo y consideramos la fase espacial $\theta(z)=kz+\mathrm{constante}$.

Al desplazarnos una longitud de onda $\lambda$, volvemos a la misma fase, un ciclo después:

$$
\begin{aligned}
\theta(z+\lambda)-\theta(z)&=2\pi,\\
k(z+\lambda)-kz&=2\pi,\\
k\lambda&=2\pi.
\end{aligned}
$$

Por tanto:

$$
\boxed{k=\frac{2\pi}{\lambda}},\qquad [k]=\mathrm{rad/m}.
$$

**Distinguir las convenciones:**

| Magnitud | Expresión | Significado |
|---|---|---|
| Frecuencia espacial | $1/\lambda$ | Ciclos por metro |
| Número de onda **angular** | $k=2\pi/\lambda$ | Radianes de fase por metro |

Por ejemplo:

- Si $\lambda_A=2\,\mathrm m$, entonces $k_A=\pi\,\mathrm{rad/m}$: en dos metros se completa **un ciclo**.
- Si $\lambda_B=1\,\mathrm m$, entonces $k_B=2\pi\,\mathrm{rad/m}$: en dos metros se completan **dos ciclos**.

Una longitud de onda menor implica un número de onda angular mayor. **Cada ciclo equivale a $2\pi$ radianes, no a un radián.**

## 4. ¿Cómo aparece la rapidez de propagación?

Una cresta avanza una longitud de onda $\lambda$ en un período $T$:

$$
\boxed{v=\frac{\lambda}{T}=\lambda f}.
$$

En términos de frecuencia angular y número de onda:

$$
\boxed{v=\frac{\omega}{k}}.
$$

También puede deducirse siguiendo una **fase constante**:

$$
\begin{aligned}
kz-\omega t+\varphi&=\text{constante},\\
k\frac{dz}{dt}-\omega&=0,\\
\frac{dz}{dt}&=\frac{\omega}{k}.
\end{aligned}
$$

Esta es la rapidez de fase de una onda armónica viajera. Para este modelo simple es la rapidez con que avanza una cresta; no debe confundirse automáticamente con la velocidad de un pulso en cualquier medio dispersivo.

**Comprobación de unidades:**

$$
[\lambda f]=\mathrm m\,\mathrm s^{-1},\qquad
\left[\frac{\omega}{k}\right]
=\frac{\mathrm{rad/s}}{\mathrm{rad/m}}
=\mathrm{m/s}.
$$

## 5. Tabla de consulta rápida

| Símbolo | Qué representa | Unidad SI | Relación |
|---|---|---|---|
| $T$ | Tiempo de un ciclo | $\mathrm s$ | $T=1/f$ |
| $f$ | Ciclos por segundo | $\mathrm{Hz}$ | $f=1/T$ |
| $\omega$ | Fase por segundo | $\mathrm{rad/s}$ | $\omega=2\pi f$ |
| $\lambda$ | Distancia de un ciclo | $\mathrm m$ | $\lambda=v/f$ |
| $k$ | Fase por metro | $\mathrm{rad/m}$ | $k=2\pi/\lambda$ |
| $v$ | Rapidez de propagación | $\mathrm{m/s}$ | $v=\lambda f=\omega/k$ |

> [!important] No confundir
> - $\omega$ y $k$ se refieren a **cambio de fase**, pero uno es temporal y el otro espacial.
> - Conocer la frecuencia $f$ **no basta** para conocer $\lambda$: también necesitamos la rapidez $v$ o información espacial equivalente.
> - Un argumento como $kz-\omega t+\varphi$ debe ser adimensional; los radianes son adimensionales en el SI.
> - La **amplitud** $A$ no es, en general, el valor instantáneo $u(z,t)$.

## 6. Recuperación activa — sin mirar las fórmulas

1. Explica cómo medirías experimentalmente $T$ y $\lambda$ usando una misma onda. ¿Qué mantienes fijo en cada caso?
2. Reconstruye $k=2\pi/\lambda$ a partir de exigir que la fase cambie un ciclo completo al recorrer $\lambda$.
3. Una onda tiene $\lambda=0.5\,\mathrm m$ y $f=20\,\mathrm{Hz}$. Encuentra $T$, $\omega$, $k$ y $v$; verifica sus unidades.
4. Si conocemos únicamente que una onda completa 8 ciclos en 2 segundos, ¿podemos determinar $\lambda$? Justifica qué dato faltaría.
5. En $u(z,t)=A\cos(kz-\omega t+\varphi)$, explica qué cambia si duplicamos $k$ sin modificar $\omega$.

## 7. Tarjetas Anki Bridge

¿Qué diferencia hay entre el período y la longitud de onda? ⇢%%oab:basic:v1%%El período $T$ es el tiempo entre estados equivalentes sucesivos en una posición fija; la longitud de onda $\lambda$ es la distancia entre puntos equivalentes sucesivos en un instante fijo.

¿Qué expresa físicamente la frecuencia angular $\omega$ de una oscilación? ⇢%%oab:basic:v1%%El cambio de fase temporal por segundo: $\omega=2\pi/T=2\pi f$, en rad/s.

¿Qué expresa el número de onda angular $k$ y de dónde sale el factor $2\pi$? ⇢%%oab:basic:v1%%Mide el cambio de fase por metro. Al recorrer una longitud de onda la fase cambia $2\pi$ rad, así que $k\lambda=2\pi$ y $k=2\pi/\lambda$.

¿Cómo se distinguen $1/\lambda$ y $k=2\pi/\lambda$? ⇢%%oab:basic:v1%%$1/\lambda$ mide ciclos por metro; $k$ mide radianes de fase por metro. Un ciclo equivale a $2\pi$ radianes.

¿Por qué no se puede determinar la longitud de onda con la frecuencia solamente? ⇢%%oab:basic:v1%%Porque también hace falta la rapidez de propagación $v$ (o información espacial equivalente): $\lambda=v/f$.

¿Cómo se relacionan la rapidez, el período y la longitud de onda de una onda armónica viajera? ⇢%%oab:basic:v1%%Una fase completa avanza $\lambda$ en un período $T$: $v=\lambda/T=\lambda f=\omega/k$.

## 8. Conexiones con otros conceptos

- [[Fasores e impedancias]] — fase y exponenciales complejas; en ondas añadimos dependencia espacial.
- **Siguiente sección:** ecuación de onda electromagnética plana; dirección de propagación; relación entre $\vec E$, $\vec B$ y la velocidad en el vacío.
