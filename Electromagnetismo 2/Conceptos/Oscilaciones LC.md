---
tags:
  - electromagnetismo-ii
  - certamen-2
  - circuitos-lc
  - oscilaciones
estado: estudiado
fuente: "Contenido 4.2 510238 Circuito RL(+C)-Oscilaciones, diapositivas 8–19"
---

> [!abstract] Pregunta física
> ¿Por qué un capacitor inicialmente cargado, conectado con un inductor ideal, puede oscilar sin una fuente externa y cómo se obtiene matemáticamente $q(t)$?

## 1. Idea física

En un **circuito LC ideal** (sin resistencia ni fuente después de cerrar el circuito), la energía se intercambia entre el campo eléctrico del capacitor y el campo magnético del inductor.

- Al comienzo: capacitor con carga $+Q$, corriente cero, energía eléctrica máxima.
- Al primer cuarto de período: capacitor descargado, corriente de magnitud máxima, energía magnética máxima.
- Al medio período: capacitor cargado con **polaridad invertida** ($-Q$), corriente cero.
- El proceso se repite: la energía no desaparece cuando $q=0$ porque sigue almacenada en el inductor.

![[energia-lc.svg]]

## 2. Leyes, hipótesis y convenciones

- Capacitor ideal: $v_C=q/C$; energía $U_E=q^2/(2C)$.
- Inductor ideal: $v_L=L\,di/dt$ en convención pasiva; energía $U_B=Li^2/2$.
- **Convención principal de esta nota (diapositiva 11 del profesor):** $q$ es la carga de la placa inicialmente positiva e $i=dq/dt$. La primera descarga tiene entonces **corriente negativa**.
- **Convención alternativa que usamos al razonar la física:** si definimos positiva la corriente de la primera descarga, $i_{\mathrm{desc}}=-dq/dt=-i$. Ambas describen el mismo fenómeno: ¡no mezclar sus signos!
- Los parámetros $L,C>0$ son constantes, y no hay resistencia, pérdidas ni excitación externa.

## 3. Desarrollo matemático

### 3.1 Ecuación diferencial

Por la ley de voltajes de Kirchhoff, con orientaciones consistentes:

$$
v_L+v_C=0
\quad\Longrightarrow\quad
L\frac{di}{dt}+\frac qC=0.
$$

Usando la convención del profesor $i=dq/dt$:

$$
L\frac{d^2q}{dt^2}+\frac qC=0
\quad\Longrightarrow\quad
\boxed{q''(t)+\omega_0^2 q(t)=0},
$$

donde

$$
\boxed{\omega_0=\frac1{\sqrt{LC}}},\qquad
\boxed{T=2\pi\sqrt{LC}},\qquad
f_0=\frac1{2\pi\sqrt{LC}}.
$$

Es la ecuación de un oscilador armónico simple. $\omega_0$ es la **frecuencia angular natural de oscilación libre** (no confundir automáticamente con todas las frecuencias características de un RLC amortiguado o mixto).

### 3.2 Solución mediante transformada de Laplace

Sean $q(0)=q_0$, $\dot q(0)=i_0$. Denotamos $\widetilde q(s)=\mathcal L\{q(t)\}$. Utilizamos

$$
\mathcal L\{q''\}=s^2\widetilde q(s)-sq_0-i_0.
$$

Transformando la EDO:

$$
(s^2+\omega_0^2)\widetilde q(s)=sq_0+i_0
\quad\Longrightarrow\quad
\widetilde q(s)=q_0\frac{s}{s^2+\omega_0^2}+\frac{i_0}{\omega_0}\frac{\omega_0}{s^2+\omega_0^2}.
$$

Aplicando $\mathcal L^{-1}$ a cada término:

$$
\boxed{q(t)=q_0\cos(\omega_0t)+\frac{i_0}{\omega_0}\sin(\omega_0t)}.
$$

**Interpretación:** el coseno está determinado por la **carga inicial**; el seno por la **corriente inicial**. Ambos pertenecen a la misma oscilación y fijan su amplitud y fase.

### 3.3 Condiciones iniciales de nuestro caso

Capacitor inicialmente cargado y circuito sin corriente:

$$
q(0)=Q,\qquad i(0)=\dot q(0)=0.
$$

Por lo tanto:

$$
\boxed{q(t)=Q\cos(\omega_0t)},
$$

$$
\boxed{i(t)=\dot q(t)=-Q\omega_0\sin(\omega_0t)}.
$$

El máximo de la **magnitud** de corriente es $I_{\max}=Q\omega_0=Q/\sqrt{LC}$; el signo negativo del primer cuarto de período solo indica sentido según la convención elegida.

> [!warning] Signo de la corriente
> Si definimos $i_{\mathrm{desc}}=-dq/dt$, la misma solución física se escribe $i_{\mathrm{desc}}=+Q\omega_0\sin(\omega_0t)$. Ambas son correctas. La diapositiva 11 del profesor utiliza $i=dq/dt$.

**Método alternativo:** al proponer $q=e^{rt}$ en la EDO se obtiene $r^2+\omega_0^2=0$, raíces $r=\pm j\omega_0$ y solución $A\cos(\omega_0t)+B\sin(\omega_0t)$. Como la EDO es homogénea, no requiere una solución particular no trivial.

### 3.4 Conservación de energía

$$
U_E=\frac{q^2}{2C}=\frac{Q^2}{2C}\cos^2(\omega_0t)
$$

$$
U_B=\frac12 Li^2=\frac12 LQ^2\omega_0^2\sin^2(\omega_0t)
=\frac{Q^2}{2C}\sin^2(\omega_0t),
$$

porque $L\omega_0^2=1/C$. Así:

$$
\boxed{U_E+U_B=\frac{Q^2}{2C}\left[\cos^2(\omega_0t)+\sin^2(\omega_0t)\right]=\frac{Q^2}{2C}}.
$$

No hay pérdida de energía: únicamente cambia dónde está almacenada.

## 4. Interpretación y comprobaciones

| Tiempo | $q$ | $i=dq/dt$ | $\mathcal E_{\mathrm{ind}}=-L\,di/dt$ | Energía máxima en |
| --- | ---: | ---: | ---: | --- |
| $0$ | $+Q$ | $0$ | positiva | Capacitor |
| $T/4$ | $0$ | $-I_{\max}$ | $0$ | Inductor |
| $T/2$ | $-Q$ | $0$ | negativa | Capacitor |
| $3T/4$ | $0$ | $+I_{\max}$ | $0$ | Inductor |
| $T$ | $+Q$ | $0$ | positiva | Capacitor |

- **Frecuencia angular:** $[LC]=\mathrm{s}^2$, por tanto $[\omega_0]=\mathrm{s}^{-1}$ (se suele escribir rad/s).
- **Corriente cero no implica fem cero:** cuando la carga del capacitor es extrema, $i=0$ pero $di/dt\neq0$.
- **Corriente máxima implica fem cero en ese instante:** la derivada $di/dt=0$, aunque el campo magnético sea máximo.
- **Energías al 50 %:** no son un equilibrio; si $i\ne0$ sigue cambiando la carga del capacitor.

## 5. En mis palabras

> [!note] Explicación personal
> Intenta describir sin mirar por qué la corriente no se detiene cuando el capacitor llega a $q=0$, y qué ocurre después.

## 6. Qué debo poder deducir sin consultar

- [ ] Fijar y mantener una convención consistente para $q$ e $i$.
- [ ] Construir la EDO $q''+q/(LC)=0$ desde Kirchhoff.
- [ ] Obtener $\omega_0$ y comprobar sus unidades.
- [ ] Resolver la EDO mediante Laplace con condiciones iniciales generales $q_0,i_0$.
- [ ] Recuperar $q(t)$, $i(t)$ e $I_{\max}$ para $q_0=Q, i_0=0$.
- [ ] Demostrar $U_E+U_B=Q^2/(2C)$.

## 7. Recuperación activa

1. **Conceptual:** en $T/4$, ¿por qué siguen circulando cargas si $v_C=0$?
2. **Deducción:** obtén la EDO desde Kirchhoff; resuélvela por Laplace para $q(0)=Q,i(0)=0$.
3. **Signos:** ¿por qué el profesor obtiene $i(t)<0$ en la primera descarga, aunque la corriente realmente circule?
4. **Variación inicial:** si $q(0)=0$ e $i(0)=I_0$, ¿qué término de la solución permanece?
5. **Conservación:** sustituye $q(t)$ e $i(t)$ en $U_E+U_B$ y elimina la dependencia temporal.

## 8. Conexiones y dudas

- **Se relaciona con:** [[Autoinducción e inductancia]] · [[Energía magnética]] · [[Oscilaciones RLC]].
- **Próximo paso:** añadir resistencia y analizar amortiguamiento.
- **Dudas pendientes:** anotar aquí signos, fases y pasos de Laplace para repasar.

---
**Fuente principal:** presentación del profesor, *Contenido 4.2 — Circuito RL(+C)-Oscilaciones*, diapositivas 8–19. La presentación usa el método de ecuación diferencial y funciones sinusoidales; la **resolución por Laplace se incorpora como método alternativo de estudio**, a solicitud del estudiante.

<!-- INICIO TARJETAS ANKI BRIDGE C2 (agregadas sin modificar teoría) -->

### Tarjetas para Anki Bridge — Oscilaciones LC

¿Cómo compruebas las unidades de la frecuencia angular natural $\omega_0=1/\sqrt{LC}$? ⇢%%oab:basic:v1%%$[L]=\mathrm{V\,s/A}$ y $[C]=\mathrm{A\,s/V}$; por tanto $[LC]=\mathrm{s^2}$ y $[\omega_0]=\mathrm{s^{-1}}$ (rad/s).

Si en un LC ideal $U_E=U_B$, ¿por qué eso no significa que la oscilación se detenga? ⇢%%oab:basic:v1%%Igualdad de energías no implica equilibrio: la corriente sigue siendo no nula, de modo que el capacitor continúa transfiriendo carga.

Con $i=dq/dt$, ¿qué signos tienen $q$, $i$ y $di/dt$ en $t=T/2$ si $q(0)=Q>0$ e $i(0)=0$? ⇢%%oab:basic:v1%%$q=-Q$, $i=0$ y $di/dt=+Q/(LC)>0$. La corriente pasa de negativa a positiva después de ese instante.

¿Por qué la corriente puede ser máxima cuando la fem autoinducida es cero?⇢%%oab:basic:v1%%Porque la fem depende de la derivada temporal de la corriente, mientras que una corriente máxima puede tener derivada cero.

En un circuito LC, ¿cómo se relaciona la corriente con la carga de una placa según la orientación elegida? ⇢%%oab:basic:v1%%Si la corriente positiva se define entrando a la placa, $i=dq/dt$. Si se define positiva durante su descarga, $i=-dq/dt$. Ambas convenciones son válidas si se mantienen consistentemente.

¿Cuál es la transformada de Laplace de la segunda derivada de $q(t)$ y cómo incorpora las condiciones iniciales? ⇢%%oab:basic:v1%%$\mathcal L{q''(t)}=s^2\widetilde q(s)-sq(0)-q'(0)$. Las dos condiciones iniciales aparecen como términos algebraicos.

En la solución general de un LC ideal, ¿qué determinan los términos seno y coseno? ⇢%%oab:basic:v1%%En $q(t)=q(0)\cos(\omega_0t)+\frac{q'(0)}{\omega_0}\sin(\omega_0t)$, el coseno depende de la carga inicial y el seno de la corriente inicial, usando $i=dq/dt$.

<!-- FIN TARJETAS ANKI BRIDGE C2 -->

