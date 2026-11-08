---
tags:
  - electromagnetismo-ii
  - certamen-2
  - corriente-alterna
  - circuitos-rlc
estado: estudiado
fuente: "Contenido 5 — Corriente Alterna (profesor, 510238); deducción de las respuestas sinusoidales"
---

> [!abstract] Pregunta física
> ¿Cómo se relacionan el voltaje y la corriente en una resistencia, un inductor y un capacitor ideales, tanto en CC como en CA?

## 1. Las tres relaciones fundamentales

Con **convención pasiva** (la corriente entra por el terminal elegido como positivo para el voltaje), y parámetros $R$, $L$ y $C$ constantes:

| Componente | Relación válida en el tiempo | Interpretación |
|---|---|---|
| Resistencia ideal | $\boxed{v_R(t)=R\,i_R(t)}$ | Voltaje y corriente son proporcionales instantáneamente. |
| Inductor ideal | $\boxed{v_L(t)=L\,\dfrac{di_L}{dt}}$ | El voltaje depende de la rapidez de cambio de corriente. |
| Capacitor ideal | $\boxed{q(t)=C\,v_C(t)}$, $\boxed{i_C(t)=C\,\dfrac{dv_C}{dt}}$ | La corriente depende de la rapidez de cambio del voltaje. |

Para el capacitor: $v_C=q/C$ y, por conservación de carga, $i_C=dq/dt$ **según la orientación de referencia elegida**.

Estas leyes **no cambian** al pasar de corriente continua a alterna. Lo que cambia es la forma temporal del voltaje o la corriente aplicada.

## 2. Cuando el voltaje es sinusoidal

Supongamos, en cada componente por separado, un voltaje

$$
v(t)=V_m\cos(\omega t),\qquad \omega=2\pi f.
$$

La respuesta sinusoidal tiene las siguientes formas (componentes **ideales** y sin componente continua adicional):

| Componente | Corriente sinusoidal | Relación de fase |
|---|---|---|
| R | $i_R(t)=\dfrac{V_m}{R}\cos(\omega t)$ | $i$ y $v$ **en fase**. |
| L | $i_L(t)=\dfrac{V_m}{\omega L}\cos(\omega t-\pi/2)$ | **La corriente se atrasa** $90^\circ$ respecto del voltaje. |
| C | $i_C(t)=\omega C V_m\cos(\omega t+\pi/2)$ | **La corriente se adelanta** $90^\circ$ respecto del voltaje. |

### Deducciones cortas

**Inductor:** $L\,di/dt=V_m\cos(\omega t)$, de donde

$$
i_L(t)=\frac{V_m}{\omega L}\sin(\omega t)+K.
$$

Tomando $K=0$ para la respuesta sinusoidal pura y usando $\sin x=\cos(x-\pi/2)$, aparece el **atraso** de la corriente. En un inductor ideal aislado, la constante $K$ depende de la condición inicial y puede ser distinta de cero.

**Capacitor:** $i_C=C\,dv_C/dt$ da

$$
i_C(t)=-\omega C V_m\sin(\omega t)
=\omega C V_m\cos(\omega t+\pi/2).
$$

Por eso la corriente **se adelanta** al voltaje.

> [!important] No confundir los desfases
> En el **inductor**, el voltaje adelanta a la corriente. En el **capacitor**, la corriente adelanta al voltaje. En la **resistencia**, coinciden los máximos y mínimos.
>
> Un cambio del origen temporal desplaza ambas señales, pero **no cambia el desfase relativo**.

## 3. CC, CA, valores medios y eficaces

- **CC en régimen estacionario:** si $di_L/dt=0$, entonces $v_L=0$ para un inductor ideal; si $dv_C/dt=0$, entonces $i_C=0$ para un capacitor ideal. Durante la conexión o desconexión, las derivadas **pueden ser distintas de cero**, aunque la fuente sea de CC.
- **CA sinusoidal:** $v(t)$ e $i(t)$ son magnitudes **instantáneas**, no valores medios ni eficaces. Las expresiones de la tabla usan **amplitudes máximas** $V_m$ e $I_m$.
- Una sinusoide pura tiene **valor medio sobre un período igual a cero**. Su valor eficaz es $V_{\mathrm{ef}}=V_m/\sqrt2$ (análogamente $I_{\mathrm{ef}}=I_m/\sqrt2$). El eficaz no es el valor instantáneo.
- $R$, $L$ y $C$ son propiedades de los componentes en este modelo; no se convierten en «valores medios» al aplicar CA.

## 4. Comprobaciones y recuperación activa

- [ ] Deducir los tres casos sinusoidales usando solo las relaciones constitutivas.
- [ ] Dibujar dos cosenos desplazados en $\pm\pi/2$ y explicar quién adelanta a quién.
- [ ] Explicar por qué $i_L=0$ no implica necesariamente $v_L=0$.
- [ ] Distinguir amplitud, valor instantáneo, valor medio y valor eficaz.

**Conexiones:** [[Autoinducción e inductancia]] · [[Energía magnética]] · [[Oscilaciones LC]] · impedancias y fasores (próxima sección).

## 5. Tarjetas de Anki Bridge

¿Por qué en una resistencia ideal el voltaje y la corriente sinusoidales están en fase? ⇢%%oab:basic:v1%%Porque $v_R(t)=R\,i_R(t)$ con $R$ constante: la corriente es proporcional al voltaje en cada instante y ambos tienen máximos simultáneos.

En un inductor ideal, ¿cuál es la ley entre voltaje y corriente y quién adelanta a quién bajo excitación sinusoidal pura? ⇢%%oab:basic:v1%%$v_L=L\,di_L/dt$ (convención pasiva); la **tensión adelanta a la corriente** en $\pi/2$. La corriente se obtiene integrando el voltaje.

En un capacitor ideal, ¿cómo se relacionan carga, voltaje y corriente, y cuál es el desfase sinusoidal? ⇢%%oab:basic:v1%%$q=Cv_C$ e $i_C=C\,dv_C/dt$ (convención pasiva, $C$ constante). La **corriente adelanta al voltaje** en $\pi/2$.

¿Por qué no se reemplazan automáticamente $v(t)$ e $i(t)$ por valores eficaces en las leyes $v_R=Ri_R$, $v_L=L\,di_L/dt$ e $i_C=C\,dv_C/dt$? ⇢%%oab:basic:v1%%Son relaciones **instantáneas**. Los valores eficaces de señales sinusoidales se usan en relaciones de amplitud y potencia, no dentro de derivadas temporales como si fueran las funciones $v(t)$ e $i(t)$.
