---
tags:
  - electromagnetismo-ii
  - certamen-2
  - corriente-alterna
  - reactancia
  - valor-eficaz
estado: estudiado
fuente: "Contenido 5 510238 CA; Contenido 5.2 510238 Potencia CA; desarrollos y comprobaciones del estudio"
---

> [!abstract] Pregunta física
> ¿Por qué un inductor y un capacitor ideales responden de manera opuesta al variar la frecuencia de una fuente sinusoidal? ¿Qué significan amplitud, valor medio y valor eficaz?

## 1. Idea física

La **reactancia** indica cómo un elemento reactivo limita la **amplitud** de corriente ante una tensión sinusoidal de una frecuencia dada. Se mide en ohmios, pero **no equivale a disipación de energía**.

- **Inductor:** para cambiar rápidamente su corriente necesitamos mayor tensión; si la amplitud de tensión está fija, a mayor frecuencia corresponde menor amplitud de corriente.
- **Capacitor:** a tensión máxima fija, la carga máxima de sus placas es fija; una oscilación más rápida exige mayor rapidez de transferencia de carga, es decir, mayor amplitud de corriente.
- **Resistencia ideal:** su relación tensión-corriente no depende de la frecuencia en este modelo.

> [!important] Amplitud no significa promedio
> El subíndice $m$ de $V_m$, $I_m$ o $Q_m$ indica **máximo** (valor de pico de una sinusoide pura), no *medio*. La amplitud de corriente $I_m$ no es la corriente eficaz ni la media temporal.

## 2. Leyes, hipótesis y convenciones

- Elementos ideales, lineales, $R,L,C$ constantes; usamos la **convención pasiva** de signos.
- Señales sinusoidales puras de frecuencia $f>0$, con $\omega=2\pi f$, en estado estacionario sinusoidal. En el inductor se omite cualquier componente de corriente constante adicional.
- Relaciones constitutivas instantáneas:

$$
v_R(t)=Ri_R(t),\qquad v_L(t)=L\frac{di_L}{dt},\qquad i_C(t)=C\frac{dv_C}{dt},\qquad q(t)=Cv_C(t).
$$

Estas relaciones instantáneas son válidas también en CC: **no** se sustituyen sus funciones por valores medios o eficaces al derivar.

## 3. Desarrollo matemático: origen de las reactancias

Tomemos **cada componente por separado** y apliquemos la misma tensión sinusoidal:

$$
v(t)=V_m\cos(\omega t).
$$

### 3.1 Inductor

De $v_L=L\,di_L/dt$:

$$
\frac{di_L}{dt}=\frac{V_m}{L}\cos(\omega t)
\quad\Longrightarrow\quad
 i_L(t)=\frac{V_m}{\omega L}\sin(\omega t)
=\frac{V_m}{\omega L}\cos\!\left(\omega t-\frac\pi2\right).
$$

Para la parte sinusoidal, $I_{Lm}=V_m/(\omega L)$. Definimos la **reactancia inductiva positiva**:

$$
\boxed{X_L=\omega L=2\pi fL},\qquad\boxed{V_m=X_LI_{Lm}}.
$$

La corriente **se atrasa** $90^\circ$ respecto de la tensión. Con $V_m,L$ fijos, al duplicar $f$ se duplica $X_L$ y se reduce $I_{Lm}$ a la mitad.

### 3.2 Capacitor

De $i_C=C\,dv_C/dt$:

$$
i_C(t)=-\omega CV_m\sin(\omega t)
=\omega CV_m\cos\!\left(\omega t+\frac\pi2\right).
$$

Su amplitud es $I_{Cm}=\omega CV_m$. Definimos la **reactancia capacitiva positiva**:

$$
\boxed{X_C=\frac1{\omega C}=\frac1{2\pi fC}},\qquad\boxed{V_m=X_CI_{Cm}}.
$$

La corriente **se adelanta** $90^\circ$ respecto de la tensión. Con $V_m,C$ fijos, al duplicar $f$ se reduce $X_C$ a la mitad y se duplica $I_{Cm}$.

### 3.3 ¿Por qué la carga máxima no aumenta en el capacitor?

$$
q(t)=CV_m\cos(\omega t)\quad\Longrightarrow\quad\boxed{Q_m=CV_m}.
$$

Si $C$ y $V_m$ son constantes, **$Q_m$ no cambia** al duplicar la frecuencia. Lo que cambia es **el tiempo** en que se transfiere la misma carga:

$$
i_C=\frac{dq}{dt},\qquad I_{Cm}=\omega Q_m.
$$

Por eso, más frecuencia significa más amplitud de corriente, aunque no más carga máxima.

### 3.4 Comparación y dimensiones

| Elemento | Cociente de amplitudes en CA | Fase de la corriente respecto a la tensión | Al duplicar $f$ con $V_m$ fijo |
|---|---|---|---|
| $R$ ideal | $V_m/I_m=R$ | $0$ | $I_m$ no cambia |
| $L$ ideal | $V_m/I_m=X_L=\omega L$ | $-\pi/2$ | $I_m\to I_m/2$ |
| $C$ ideal | $V_m/I_m=X_C=1/(\omega C)$ | $+\pi/2$ | $I_m\to2I_m$ |

$$
[X_L]=[\omega L]=\mathrm{s^{-1}}\,\mathrm{H}=\Omega,
\quad [X_C]=[1/(\omega C)]=\Omega.
$$

> [!warning] No usar $V_m=XI_m$ como relación instantánea
> La igualdad entre amplitudes no significa $v(t)=Xi(t)$: **hay desfase**. Al combinar componentes necesitaremos fasores e impedancias complejas; allí $X_L$ y $X_C$ son magnitudes positivas, pero la impedancia inductiva tiene parte imaginaria positiva y la capacitiva negativa.

## 4. Valores instantáneo, máximo, medio y eficaz

Para una sinusoide pura (sin componente continua):

$$
v(t)=V_m\cos(\omega t+\varphi).
$$

| Nombre | Significado | Resultado |
|---|---|---|
| Instantáneo $v(t)$ | Valor en un instante; puede ser positivo o negativo | $V_m\cos(\omega t+\varphi)$ |
| Máximo o de pico $V_m$ | Máximo valor positivo; amplitud | $V_m$ |
| Medio sobre un período $\overline v$ | Promedio **algebraico** de un ciclo completo | $\dfrac1T\int_0^T v(t)dt=0$ |
| Eficaz o RMS $V_{\mathrm{ef}}$ | Raíz del promedio del cuadrado; equivalente para potencia en una resistencia | $\sqrt{\dfrac1T\int_0^T v^2(t)dt}=\dfrac{V_m}{\sqrt2}$ |

De manera análoga, para $i(t)=I_m\cos(\omega t+\varphi_i)$:

$$
\boxed{I_{\mathrm{ef}}=\frac{I_m}{\sqrt2}},\qquad \overline i=0.
$$

**Deducción del RMS:** por la identidad $\cos^2\theta=(1+\cos2\theta)/2$, el promedio de $\cos^2$ durante un período es $1/2$. Por ello,

$$
V_{\mathrm{ef}}^2=\frac1T\int_0^T V_m^2\cos^2(\omega t+\varphi)dt
=\frac{V_m^2}{2}.
$$

> [!note] Dos matices importantes
> - **Medio** y **eficaz** no son equivalentes. El promedio de una sinusoide pura sobre un período es cero, pero su valor eficaz no.
> - La media de una **semionda positiva** no es cero: $2V_m/\pi$. Siempre especificar el intervalo de promedio. El valor eficaz no es una tensión constante que realmente aparezca en el circuito.

En una resistencia, $\langle p\rangle=V_{\mathrm{ef}}I_{\mathrm{ef}}=I_{\mathrm{ef}}^2R$; esta interpretación **no se aplica como disipación** a $L$ o $C$ ideales.

## 5. Interpretación y comprobaciones

- **Límite de CC estacionaria:** para $\omega\to0^+$, $X_L\to0$ y $X_C\to\infty$. Esto no describe el transitorio de conexión.
- **Energía:** $L$ almacena $U_B=Li^2/2$ y $C$ almacena $U_E=Cv^2/2$. En régimen sinusoidal puro ambos ideales devuelven durante parte del ciclo lo que recibieron; su **potencia media neta es cero**. Una resistencia ideal disipa $Ri^2\ge0$.
- **Ejemplo de la conversación:** si un capacitor tiene $I_m=3\,\mathrm A$ y duplicamos $f$ manteniendo $C,V_m$, entonces $I_m'=6\,\mathrm A$ y $I_{\mathrm{ef}}'=6/\sqrt2\,\mathrm A$. No es necesario conocer el valor numérico de $V_m$.

## 6. En mis palabras

> [!note] Explicación personal
> ¿Por qué a mayor frecuencia la amplitud de corriente disminuye en un inductor pero aumenta en un capacitor, cuando se mantiene fijo el voltaje máximo?

## 7. Qué debo poder deducir sin consultar

- [ ] Desde $v_L=L\,di/dt$ obtener $X_L=\omega L$ y el atraso de la corriente.
- [ ] Desde $i_C=C\,dv/dt$ obtener $X_C=1/(\omega C)$ y el adelanto de la corriente.
- [ ] Diferenciar $Q_m=CV_m$ de $I_m=\omega Q_m$ y explicar el papel de la frecuencia.
- [ ] Definir valor medio sobre un período y valor eficaz; deducir $V_{\mathrm{ef}}=V_m/\sqrt2$.
- [ ] Distinguir reactancia de resistencia y comprobar unidades.

## 8. Recuperación activa

1. **Conceptual:** con $V_m$ fijo, ¿qué ocurre con la amplitud de corriente en $L$ y en $C$ al duplicar la frecuencia? Justifica sin memorizar las fórmulas.
2. **Deducción:** encuentra las dos reactancias desde las relaciones constitutivas.
3. **Conceptual:** si $Q_m$ permanece igual, ¿por qué $I_m$ puede aumentar?
4. **Deducción breve:** demuestra el factor $1/\sqrt2$ del valor eficaz de una sinusoide.
5. **Confusión frecuente:** ¿por qué $\overline i=0$ no significa que una resistencia conectada a CA no disipe potencia?

## 9. Conexiones y dudas

- **Se relaciona con:** [[Relaciones constitutivas RLC - CC y CA]] · [[Oscilaciones LC]] · [[Energía magnética]].
- **Siguiente tema:** fasores, impedancias complejas y circuitos RLC en serie.
- **Dudas pendientes:** incorporar aquí preguntas surgidas en los ejercicios de CA.

## 10. Tarjetas Anki Bridge

¿Por qué la reactancia inductiva de un inductor ideal aumenta con la frecuencia sinusoidal? ⇢%%oab:basic:v1%%Porque $v_L=L\,di/dt$: para una misma amplitud de corriente, un cambio más rápido exige más amplitud de voltaje. Por ello $X_L=\omega L$.

¿Por qué la reactancia capacitiva disminuye cuando aumenta la frecuencia sinusoidal? ⇢%%oab:basic:v1%%Para un mismo voltaje máximo, $Q_m=CV_m$ no cambia, pero la carga varía más rápido: $I_m=\omega Q_m$. Por tanto $X_C=1/(\omega C)$ disminuye.

En un capacitor ideal con $C$ y $V_m$ fijos, ¿qué cambia en $Q_m$ e $I_m$ si duplicamos la frecuencia? ⇢%%oab:basic:v1%%$Q_m=CV_m$ permanece igual; $I_m=\omega CV_m$ se duplica. Cambia la rapidez de transferencia de carga, no la carga máxima.

¿Qué diferencia hay entre valor medio y valor eficaz de una corriente sinusoidal pura durante un período? ⇢%%oab:basic:v1%%La media algebraica es $0$; el eficaz es $I_m/\sqrt2$, la corriente continua que disiparía igual potencia media en una resistencia.

¿Por qué un inductor o capacitor ideal puede tener reactancia sin disipar potencia media? ⇢%%oab:basic:v1%%Almacena energía en un campo y la devuelve durante el ciclo. En régimen sinusoidal estacionario, la potencia instantánea cambia de signo y su promedio es cero.

---

**Fuente principal:** presentaciones del profesor *Contenido 5 — CA* y *Contenido 5.2 — Potencia CA*. Las deducciones, comprobaciones y preguntas se organizan a partir de las relaciones constitutivas y de las dificultades trabajadas en esta conversación. Esta nota no reemplaza la nota anterior de relaciones RLC.
