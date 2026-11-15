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

## 1. ¿Qué problema queremos resolver?

Las relaciones constitutivas de los componentes R, L y C contienen derivadas y, en corriente alterna, sus voltajes y corrientes pueden presentar desfases.

En **régimen sinusoidal estacionario**, los fasores permiten transformar estas relaciones diferenciales en relaciones algebraicas entre números complejos.

**Condición fundamental:** las señales que se combinan mediante un único método fasorial deben tener la misma frecuencia angular.

**Notas relacionadas:**

- [[Relaciones constitutivas RLC - CC y CA]]
    
- [[Reactancias y valores maximo medio eficaz]]
    
- [[Oscilaciones LC]]
    

## 2. Las tres representaciones

Para una corriente sinusoidal:

$$  
i(t)=I_m\cos(\omega t+\varphi)  
$$

Distinguimos:

**Señal física (real):**

$$  
i(t)=I_m\cos(\omega t+\varphi)  
$$

**Representación compleja temporal:**

$$  
\underline i(t)=I_m e^{j\varphi}e^{j\omega t}  
$$

**Fasor:**

$$  
\widetilde I=I_m e^{j\varphi}=I_m\angle\varphi  
$$

La relación entre ellas es:

$$  
\boxed{\underline i(t)=\widetilde I e^{j\omega t}}  
$$

$$  
\boxed{i(t)=\operatorname{Re}[\widetilde I e^{j\omega t}]}  
$$

El fasor **no contiene el factor temporal** (e^{j\omega t}).

Aquí (j^2=-1). Utilizamos (j) para distinguir la unidad imaginaria de la corriente eléctrica.

### Módulo, argumento y valor instantáneo

Si:

$$  
\widetilde I=a+jb  
$$

entonces:

$$  
I_m=|\widetilde I|=\sqrt{a^2+b^2}  
$$

$$  
\varphi=\arg(\widetilde I)  
$$

Y, para fasores definidos con amplitudes máximas:

$$  
i(0)=\operatorname{Re}(\widetilde I)=a  
$$

**Importante:** el módulo es la amplitud; la parte real del fasor es la corriente en (t=0). No son necesariamente iguales.

### Convención con valores eficaces

También podemos definir fasores RMS:

$$  
\widetilde I_{\mathrm{ef}}=I_{\mathrm{ef}}e^{j\varphi}  
$$

En ese caso:

$$  
i(t)=\sqrt2\operatorname{Re}  
[\widetilde I_{\mathrm{ef}}e^{j\omega t}]  
$$

Debemos mantener la misma convención para todos los voltajes y corrientes. Las impedancias y los desfases no cambian al escoger valores máximos o eficaces.

## 3. ¿Por qué aparece (j\omega)?

Consideramos:

$$  
\underline i(t)=\widetilde I e^{j\omega t}  
$$

Derivando:

$$  
\frac{d\underline i}{dt}  
=\widetilde I(j\omega)e^{j\omega t}  
$$

Por tanto, el fasor de la derivada es:

$$  
\boxed{\widetilde{\left(\frac{di}{dt}\right)}  
=j\omega\widetilde I}  
$$

En el dominio fasorial:

$$  
\boxed{\frac{d}{dt}\longleftrightarrow j\omega}  
$$

**Interpretación:** multiplicar por (\omega) modifica la amplitud; multiplicar por (j) adelanta la fase (90^\circ).

Esta correspondencia se aplica a señales sinusoidales de frecuencia conocida, no a funciones arbitrarias del tiempo.

## 4. Impedancia compleja

La impedancia generaliza la relación de Ohm al régimen sinusoidal:

$$  
\boxed{\widetilde V=Z\widetilde I}  
$$

En general:

$$  
Z=R+jX  
$$

- La parte real (R) representa el comportamiento resistivo.
    
- La parte imaginaria (X) representa el comportamiento reactivo neto.
    
- El módulo (|Z|) relaciona amplitudes de voltaje y corriente.
    
- El argumento (\arg Z) es el desfase del voltaje respecto de la corriente.
    

$$  
|Z|=\frac{V_m}{I_m}  
=\frac{V_{\mathrm{ef}}}{I_{\mathrm{ef}}}  
$$

$$  
\arg Z=\varphi_V-\varphi_I  
$$

### Impedancias de componentes ideales

|Componente|Impedancia|Corriente respecto al voltaje|
|---|---|---|
|Resistor|(Z_R=R)|En fase|
|Inductor|(Z_L=j\omega L=jX_L)|Atrasada (90^\circ)|
|Capacitor|(Z_C=-j/(\omega C)=-jX_C)|Adelantada (90^\circ)|

Para el inductor:

$$  
v_L=L\frac{di_L}{dt}  
\quad\Longrightarrow\quad  
\widetilde V_L=j\omega L\widetilde I_L  
$$

Para el capacitor:

$$  
i_C=C\frac{dv_C}{dt}  
\quad\Longrightarrow\quad  
\widetilde I_C=j\omega C\widetilde V_C  
$$

**No confundir:** (X_L=\omega L) es una reactancia real positiva; (Z_L=jX_L) es una impedancia compleja.

## 5. Circuitos en serie y paralelo

### Conexión en serie

Todos los componentes comparten la misma corriente:

$$  
\widetilde V=\sum_k\widetilde V_k  
$$

Las impedancias se suman:

$$  
Z_{\mathrm{eq}}=\sum_k Z_k  
$$

Para RLC serie:

$$  
\boxed{Z=R+j(X_L-X_C)}  
$$

### Conexión en paralelo

Todos los componentes comparten el mismo voltaje:

$$  
\widetilde I=\sum_k\widetilde I_k  
$$

Las admitancias se suman:

$$  
\boxed{Y_{\mathrm{eq}}=\sum_k\frac1{Z_k}}  
$$

donde (Y=1/Z), medida en siemens ((\mathrm S=\Omega^{-1})).

Para RLC paralelo ideal:

$$  
Y=\frac1R+j\left(\frac1{X_C}-\frac1{X_L}\right)  
$$

**Regla algebraica:** sumar números complejos en forma rectangular (a+jb); multiplicar o dividir resulta más cómodo en forma polar (M\angle\varphi).

Nunca sumar directamente módulos de corrientes desfasadas como si fueran números escalares.

## 6. Resonancia en un circuito RLC serie

Cuando:

$$  
X_L=X_C  
$$

la parte imaginaria de la impedancia se anula:

$$  
Z=R  
$$

La corriente y el voltaje de la fuente quedan en fase y, para (R>0) y voltaje de amplitud fija, la amplitud de corriente alcanza su máximo:

$$  
I_{m,\mathrm{res}}=\frac{V_m}{R}  
$$

La corriente sigue siendo sinusoidal: **que su amplitud sea máxima no significa que su valor instantáneo sea constante**.

## 7. Componentes reales

Una bobina real puede modelarse aproximadamente mediante una resistencia interna (R_L) en serie con una inductancia ideal:

$$  
\boxed{Z_{\mathrm{bobina}}=R_L+j\omega L}  
$$

La resistencia interna disipa energía; la parte inductiva ideal almacena y devuelve energía magnética.

Para esa bobina:

$$  
I_{\mathrm{ef}}=\frac{V_{\mathrm{ef}}}  
{\sqrt{R_L^2+(\omega L)^2}}  
$$

No podemos reemplazar (|Z|) por (X_L) si las pérdidas resistivas no son despreciables.

Este modelo es una aproximación: otros componentes reales pueden requerir circuitos equivalentes diferentes.

## 8. Comprobaciones y errores importantes

**Errores que aparecieron durante los ejercicios:**

- Confundir el fasor (\widetilde I) con la representación compleja temporal (\underline i(t)).
    
- Interpretar un módulo conocido (|\widetilde I|) como si fuera un fasor real con fase cero.
    
- Confundir (X_L) con (Z_L=jX_L).
    
- Sumar módulos de corrientes desfasadas en lugar de sus fasores.
    
- Utilizar la impedancia de un componente ideal para modelar uno con pérdidas resistivas.
    
- Redondear resultados intermedios antes de resolver todo el sistema.
    

**Unidades que conviene revisar:**

|Prefijo|Factor|
|---|---|
|mili (m)|(10^{-3})|
|micro (µ)|(10^{-6})|
|nano (n)|(10^{-9})|

$$  
1,\mathrm{mA}=0.001,\mathrm A  
$$

$$  
1,\mathrm H=1,\Omega\cdot\mathrm s  
$$

$$  
1,\mathrm F=\frac{\mathrm s}{\Omega}  
$$

Antes de aceptar un resultado, comprobar las unidades, el cuadrante del número complejo y si el comportamiento es inductivo o capacitivo.

## 9. Recuperación activa

Sin consultar las deducciones anteriores:

1. Reconstruir la impedancia inductiva desde su relación constitutiva.
    
2. Reconstruir la impedancia capacitiva mediante fasores.
    
3. Explicar la diferencia entre fasor, representación compleja temporal y señal física.
    
4. Deducir por qué se suman impedancias en serie y admitancias en paralelo.
    
5. Explicar por qué el módulo de una corriente total no es, en general, la suma de los módulos de las corrientes de sus ramas.
    

## 10. Tarjetas Anki Bridge

```
¿Qué conserva un fasor de una señal sinusoidal de frecuencia conocida? ⇢%%oab:basic:v1%%Su amplitud y fase inicial; el factor temporal común se representa aparte.

Para fasores definidos con amplitudes máximas, ¿cómo se obtiene la amplitud de corriente? ⇢%%oab:basic:v1%%Mediante el módulo del fasor: \(I_m=|\widetilde I|\).

¿Por qué una derivada temporal se representa mediante \(j\omega\) en análisis fasorial? ⇢%%oab:basic:v1%%Porque derivar el factor \(e^{j\omega t}\) produce \(j\omega e^{j\omega t}\).

¿Qué distingue la reactancia inductiva de la impedancia inductiva? ⇢%%oab:basic:v1%%\(X_L=\omega L\) es real positiva; \(Z_L=jX_L\) incorpora además el desfase.

¿Cómo se relaciona la corriente de un capacitor ideal con el voltaje sinusoidal? ⇢%%oab:basic:v1%%La corriente adelanta al voltaje \(90^\circ\); \(Z_C=-j/(\omega C)\).

¿Qué se suma en análisis fasorial de circuitos serie y paralelo? ⇢%%oab:basic:v1%%En serie se suman impedancias; en paralelo, admitancias.

¿Por qué no basta la reactancia para calcular la corriente de una bobina real? ⇢%%oab:basic:v1%%Porque su resistencia interna también contribuye al módulo de la impedancia y disipa energía.
```