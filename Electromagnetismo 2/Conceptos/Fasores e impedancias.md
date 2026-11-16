---
tags:
  - electromagnetismo-ii
  - corriente-alterna
  - fasores
  - impedancia
aliases:
  - Método fasorial
---

# Fasores e impedancias

> [!abstract] Propósito
> Comprender por qué podemos resolver circuitos de corriente alterna sinusoidal con números complejos, qué representa cada símbolo y cuándo conviene sumar impedancias o admitancias.

**Conexiones:** [[Relaciones constitutivas RLC - CC y CA]] · [[Reactancias y valores maximo medio eficaz]] · [[Oscilaciones LC]]

## 1. ¿Qué problema resolvemos?

Las relaciones de los componentes $R$, $L$ y $C$ contienen derivadas y relacionan señales sinusoidales con posibles desfases. En **régimen sinusoidal estacionario**, la representación fasorial convierte las ecuaciones diferenciales en relaciones algebraicas.

**Condición:** para combinar señales mediante una sola suma de fasores, todas deben tener la misma frecuencia angular $\omega$. El método no describe por sí solo los transitorios.

## 2. Tres representaciones distintas

Consideremos una corriente sinusoidal:

$$
i(t)=I_m\cos(\omega t+\varphi).
$$

- **Señal física real:** $i(t)=I_m\cos(\omega t+\varphi)$.
- **Representación compleja temporal:** $\underline i(t)=I_m e^{j\varphi}e^{j\omega t}$.
- **Fasor de amplitud máxima:** $\widetilde I=I_m e^{j\varphi}=I_m\angle\varphi$.

Por tanto:

$$
\boxed{\underline i(t)=\widetilde I e^{j\omega t}},\qquad
\boxed{i(t)=\operatorname{Re}[\widetilde I e^{j\omega t}]}.
$$

Usamos $j^2=-1$ para no confundir la unidad imaginaria con la corriente eléctrica.

El **fasor no contiene** $e^{j\omega t}$: conserva el módulo y la fase inicial de la señal. La parte imaginaria es una herramienta matemática que **no se descarta durante las operaciones**; se toma la parte real al recuperar la señal física.

### Módulo, parte real y fase inicial

Para $\widetilde I=a+jb$:

$$
\boxed{I_m=|\widetilde I|=\sqrt{a^2+b^2}},\qquad
\varphi=\arg(\widetilde I),\qquad
\boxed{i(0)=\operatorname{Re}(\widetilde I)=a}.
$$

**Error frecuente:** el módulo del fasor **no** es su parte real. Por ejemplo, si $\widetilde I=3+4j\,\mathrm A$, la amplitud es $5\,\mathrm A$ pero $i(0)=3\,\mathrm A$.

### Fasores con valores eficaces (RMS)

También se puede definir $\widetilde I_{\mathrm{ef}}=I_{\mathrm{ef}}e^{j\varphi}$; en tal caso:

$$
i(t)=\sqrt2\operatorname{Re}[\widetilde I_{\mathrm{ef}}e^{j\omega t}].
$$

Para senoidales puras, $I_{\mathrm{ef}}=I_m/\sqrt2$ y $V_{\mathrm{ef}}=V_m/\sqrt2$. Usar **una sola convención** en todo el circuito. Las impedancias y los desfases son iguales con amplitudes máximas o eficaces.

## 3. ¿Por qué derivar equivale a multiplicar por $j\omega$?

Desde la representación compleja temporal:

$$
\underline i(t)=\widetilde I e^{j\omega t}
$$

$$
\frac{d\underline i}{dt}
=\widetilde I\frac{d}{dt}e^{j\omega t}
=j\omega\widetilde I e^{j\omega t}.
$$

Identificando el fasor de la derivada:

$$
\boxed{\widetilde{\left(\frac{di}{dt}\right)}=j\omega\widetilde I}
\qquad\Longrightarrow\qquad
\frac{d}{dt}\ \longleftrightarrow\ j\omega.
$$

Multiplicar por $\omega$ escala la amplitud; multiplicar por $j=e^{j\pi/2}$ adelanta la fase $90^\circ$. Esta correspondencia requiere una señal sinusoidal de frecuencia fija: no vale para cualquier función temporal.

## 4. Impedancia compleja: amplitud y desfase juntos

Definimos:

$$
\boxed{\widetilde V=Z\widetilde I},\qquad
\boxed{Z=\frac{\widetilde V}{\widetilde I}}.
$$

En general, $Z=R+jX$, medida en ohmios. Su módulo relaciona las amplitudes o valores eficaces y su argumento indica el desfase:

$$
|Z|=\frac{V_m}{I_m}=\frac{V_{\mathrm{ef}}}{I_{\mathrm{ef}}},\qquad
\arg Z=\varphi_V-\varphi_I.
$$

| Componente ideal | Ley temporal | Impedancia | Corriente respecto del voltaje |
|---|---|---|---|
| Resistencia | $v_R=Ri_R$ | $Z_R=R$ | En fase |
| Inductor | $v_L=L\,di_L/dt$ | $Z_L=j\omega L=jX_L$ | Se atrasa $90^\circ$ |
| Capacitor | $i_C=C\,dv_C/dt$ | $Z_C=1/(j\omega C)=-jX_C$ | Se adelanta $90^\circ$ |

**Diferencia esencial:** $X_L=\omega L$ y $X_C=1/(\omega C)$ son reactancias reales positivas; las impedancias $Z_L=jX_L$ y $Z_C=-jX_C$ incluyen el signo de fase.

### Deducción mínima, no solo memorización

Inductor:

$$
v_L=L\frac{di_L}{dt}
\quad\longrightarrow\quad
\widetilde V_L=j\omega L\widetilde I_L
\quad\longrightarrow\quad
Z_L=j\omega L.
$$

Capacitor:

$$
i_C=C\frac{dv_C}{dt}
\quad\longrightarrow\quad
\widetilde I_C=j\omega C\widetilde V_C
\quad\longrightarrow\quad
Z_C=\frac{1}{j\omega C}=-\frac{j}{\omega C}.
$$

## 5. ¿Cómo se combinan los componentes?

### Serie

La **corriente** es común; los voltajes se suman fasorialmente:

$$
\widetilde V_{\mathrm{tot}}=\sum_k\widetilde V_k,
\qquad
Z_{\mathrm{eq}}=\sum_k Z_k.
$$

Para RLC serie:

$$
\boxed{Z_{\mathrm{eq}}=R+j(X_L-X_C)}.
$$

### Paralelo

El **voltaje** es común; las corrientes se suman fasorialmente:

$$
\widetilde I_{\mathrm{tot}}=\sum_k\widetilde I_k.
$$

Definimos la **admitancia** $Y=1/Z$ (unidad: siemens, $\mathrm S=\Omega^{-1}$); en paralelo:

$$
\boxed{Y_{\mathrm{eq}}=\sum_k Y_k=\sum_k\frac1{Z_k}}.
$$

En un RLC paralelo ideal:

$$
Y_{\mathrm{eq}}=\frac1R+j\left(\frac1{X_C}-\frac1{X_L}\right).
$$

**Regla operativa:** para sumar, usar forma rectangular $a+jb$; para multiplicar o dividir, suele convenir la forma polar $M\angle\varphi$. **No sumar directamente módulos** de corrientes desfasadas.

## 6. Resonancia RLC serie

La condición de resonancia es $X_L=X_C$, de donde:

$$
Z=R,\qquad \varphi_Z=0,\qquad
\boxed{I_{m,\mathrm{res}}=\frac{V_m}{R}}
$$

(Con $R>0$ y $V_m$ fijo.) La corriente queda en fase con el voltaje; **su amplitud** es máxima, pero su valor instantáneo continúa oscilando.

## 7. Bobina real y modelos equivalentes

Una bobina real puede modelarse aproximadamente como resistencia interna $R_L$ en serie con inductancia ideal $L$:

$$
\boxed{Z_{\mathrm{bobina}}=R_L+j\omega L},\qquad
|Z_{\mathrm{bobina}}|=\sqrt{R_L^2+(\omega L)^2}.
$$

La resistencia produce pérdidas por efecto Joule; el comportamiento inductivo ideal almacena y devuelve energía magnética. Por ello, **no** corresponde usar $I_{\mathrm{ef}}=V_{\mathrm{ef}}/X_L$ para una bobina real con resistencia no despreciable. El modelo apropiado para otros componentes reales depende del tipo de pérdidas.

## 8. Unidades y errores detectados

| Unidad/prefijo | Equivalencia |
|---|---|
| $\mathrm{mA}$ | $10^{-3}\,\mathrm A$ |
| $\mu\mathrm A$ | $10^{-6}\,\mathrm A$ |
| $\mathrm{nA}$ | $10^{-9}\,\mathrm A$ |
| Henrio | $1\,\mathrm H=1\,\Omega\,\mathrm s$ |
| Faradio | $1\,\mathrm F=1\,\mathrm s/\Omega$ |
| Siemens | $1\,\mathrm S=1/\Omega$ |

Errores que aparecieron durante el estudio:

- Confundir $i(t)$ con $\underline i(t)$ o con $\widetilde I$.
- Interpretar que conocer $|\widetilde I|$ equivale a conocer $\widetilde I$ completo.
- Confundir **módulo** (amplitud) con **parte real** (valor instantáneo a $t=0$, si se usan fasores máximos).
- Omitir el factor $j$ al identificar $X_L$ con $Z_L$.
- Sumar módulos de corrientes que tienen fases diferentes.
- Usar únicamente reactancia para una bobina con pérdidas resistivas.
- Redondear resultados intermedios demasiado pronto.
- Mezclar grados y radianes al escribir el argumento de un coseno.

## 9. Recuperación activa

1. Sin consultar las ecuaciones, obtener $Z_L$ desde la ley temporal del inductor.
2. Obtener $Z_C$ desde la ley temporal del capacitor.
3. Dado $\widetilde I=3+4j\,\mathrm A$, hallar $I_m$, $i(0)$ y la corriente temporal.
4. Explicar por qué se suman **impedancias** en serie y **admitancias** en paralelo.
5. Plantear un circuito de dos situaciones para obtener la resistencia interna y la inductancia de una bobina real.

## 10. Tarjetas Anki Bridge

¿Qué conserva un fasor de una señal sinusoidal de frecuencia conocida? ⇢%%oab:basic:v1%%Su amplitud y fase inicial; el factor temporal común se representa aparte.

Para fasores definidos con amplitudes máximas, ¿cómo se obtiene la amplitud de corriente? ⇢%%oab:basic:v1%%Mediante el módulo del fasor: $I_m=|\widetilde I|$.

¿Por qué una derivada temporal se representa mediante $j\omega$ en análisis fasorial? ⇢%%oab:basic:v1%%Porque derivar el factor $e^{j\omega t}$ produce $j\omega e^{j\omega t}$.

¿Qué distingue la reactancia inductiva de la impedancia inductiva? ⇢%%oab:basic:v1%%$X_L=\omega L$ es real positiva; $Z_L=jX_L$ incorpora además el desfase.

¿Cómo se relaciona la corriente de un capacitor ideal con el voltaje sinusoidal? ⇢%%oab:basic:v1%%La corriente adelanta al voltaje $90^\circ$; $Z_C=-j/(\omega C)$.

¿Qué se suma en análisis fasorial de circuitos serie y paralelo? ⇢%%oab:basic:v1%%En serie se suman impedancias; en paralelo, admitancias.

¿Por qué no basta la reactancia para calcular la corriente de una bobina real? ⇢%%oab:basic:v1%%Porque su resistencia interna también contribuye al módulo de la impedancia y disipa energía.
