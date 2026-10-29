---
tags:
  - laboratorio-1
  - conceptos
  - estadistica
  - incertidumbres
tipo: concepto
asignatura: "Laboratorio 1"
unidad: "Medidas estadísticas y propagación de incertidumbres"
estado: practicar
fuente: "Clase 3_Medidas estadísticas.pdf (diapositivas 1-24)"
---

# Clase 3 — Medidas estadísticas y propagación de incertidumbres

> [!abstract] Pregunta central
> Si repetimos una medición y obtenemos resultados diferentes, ¿cómo estimamos la magnitud y su incertidumbre? Si luego calculamos una función de varias mediciones, ¿cómo se transmite esa incertidumbre?

> [!info] Cómo usar esta nota
> **Primero** intenta reconstruir las ideas de los apartados 1–4. **Después** resuelve los ejercicios del apartado 7 sin consultar. El ejercicio de densidad queda **pendiente y sin respuesta**, para practicarlo en la próxima sesión.

## 1. Idea e interpretación intuitiva

Una serie de mediciones de una magnitud no suele arrojar exactamente el mismo número. La estadística permite responder **dos preguntas diferentes**:

- **¿Dónde se concentran las mediciones?** → media y mediana.
- **¿Cuánto varían y con qué precisión estimamos el promedio?** → varianza, desviación estándar y error estándar del promedio.

Si además una magnitud se obtiene indirectamente, por ejemplo $\rho=m/V$, las incertidumbres de $m$ y $V$ afectan a $\rho$. Para estimar ese efecto utilizamos la **propagación de incertidumbres**.

> [!important] No confundir
> La media caracteriza el **centro**, $\sigma$ caracteriza la **dispersión de las mediciones individuales** y $\delta\bar{x}$ caracteriza la **incertidumbre estadística del promedio**. Son objetos distintos.

## 2. Fundamentos, hipótesis y convenciones

### 2.1. Notación

| Símbolo | Significado | Unidad |
|---|---|---|
| $x_i$ | Medición individual | Unidad de $x$ |
| $N$ | Número de mediciones | Adimensional |
| $\bar{x}$ | Media aritmética | Unidad de $x$ |
| $\tilde{x}$ | Mediana | Unidad de $x$ |
| $\sigma^2$ | Varianza según la fórmula de la presentación | Unidad de $x$ al cuadrado |
| $\sigma$ | Desviación estándar | Unidad de $x$ |
| $\delta\bar{x}$ | Error estándar del promedio | Unidad de $x$ |
| $\delta f$ | Incertidumbre de una función calculada | Unidad de $f$ |

- **Fuente principal:** presentación del profesor, diapositivas 2–20 (estadística) y 22–24 (propagación).
- **Convención del profesor:** para la varianza de los datos utiliza el denominador $N$; en estadística inferencial también aparece la varianza muestral corregida con $N-1$. No intercambiar ambas sin revisar el criterio del problema.
- **Error estándar:** la reducción como $1/\sqrt{N}$ supone mediciones independientes y una dispersión del proceso estable; repetir mediciones **no corrige** un error sistemático.
- **Propagación por Taylor:** se trabaja a primer orden, suponiendo incertidumbres suficientemente pequeñas para despreciar términos superiores.
- **Propagación cuadrática:** la fórmula de la diapositiva 24 presupone variables independientes; en general, cuando hay correlaciones, aparecen términos de covarianza (ampliación, no desarrollada por la presentación).

## 3. Desarrollo matemático o procedimiento

### 3.1. Valores medios (diapositivas 2–6)

La **media aritmética** de $N$ mediciones es:

$$
\boxed{\bar{x}=\frac{1}{N}\sum_{i=1}^{N}x_i}.
$$

La **mediana** es el valor central de los datos **ordenados**. Si $N$ es par, se promedian los dos valores centrales. Es menos sensible a los valores extremos que la media.

**Ejemplo que practicamos:** para $9{,}8$, $9{,}9$, $10{,}0$, $10{,}1$, $12{,}2\,\mathrm{cm}$:

$$
\bar{x}=10{,}4\,\mathrm{cm},\qquad \tilde{x}=10{,}0\,\mathrm{cm}.
$$

El dato $12{,}2\,\mathrm{cm}$ eleva la media, pero no desplaza la mediana en este conjunto.

### 3.2. Histograma y distribución (diapositivas 7–8)

El **histograma** reúne mediciones cuantitativas en intervalos y muestra sus frecuencias. La presentación compara histogramas de temperatura usando intervalos de $1$, $0{,}5$ y $0{,}1\,^{\circ}\mathrm C$: el ancho elegido cambia la apariencia de la distribución, aunque los datos sean los mismos.

Conecta con [[Clase 1 - Graficos experimentales]].

### 3.3. Varianza y desviación estándar (diapositivas 9–10)

Primero calculamos los **residuos** respecto de la media:

$$
r_i=x_i-\bar{x}.
$$

Los residuos suman cero, por lo que no sirve usar su suma como indicador de dispersión. Elevamos al cuadrado y promediamos:

$$
\boxed{\sigma^2=\frac{1}{N}\sum_{i=1}^{N}(x_i-\bar{x})^2}.
$$

Para recuperar las unidades originales, tomamos la raíz cuadrada:

$$
\boxed{\sigma=\sqrt{\frac{1}{N}\sum_{i=1}^{N}(x_i-\bar{x})^2}}.
$$

**Ejemplo que practicamos:** dos series con la misma media $10\,\mathrm{cm}$:

| Serie | Mediciones (cm) | Varianza (cm²) | Desviación estándar (cm) |
|---|---|---|---|
| A | $9,10,11$ | $2/3\approx0{,}667$ | $\sqrt{2/3}\approx0{,}816$ |
| B | $7,10,13$ | $6$ | $\sqrt 6\approx2{,}449$ |

La serie B es **menos precisa** porque tiene mayor dispersión. Que los datos estén separados por $3\,\mathrm{cm}$ **no significa** que su desviación estándar sea $3\,\mathrm{cm}$.

### 3.4. Error estándar del promedio (diapositivas 11–16)

$$
\boxed{\delta\bar{x}=\frac{\sigma}{\sqrt{N}}}.
$$

- $\sigma$: dispersión característica de las mediciones **individuales**.
- $\delta\bar{x}$: incertidumbre estadística de la **media**.

Si $\sigma$ permanece aproximadamente constante, cuadruplicar $N$ reduce $\delta\bar{x}$ a la **mitad**, no a la cuarta parte.

**Ejemplo que practicamos:** con $\sigma=2{,}4\,\mathrm{cm}$:

$$
N=4:\quad\delta\bar{x}=\frac{2{,}4}{\sqrt4}=1{,}2\,\mathrm{cm},
$$

$$
N=16:\quad\delta\bar{x}=\frac{2{,}4}{\sqrt{16}}=0{,}6\,\mathrm{cm}.
$$

En la presentación, una estimación obtenida de mediciones repetidas se informa como:

$$
\boxed{\bar{x}\pm\delta\bar{x}}.
$$

> [!warning] Atención al redondeo de las diapositivas
> La diapositiva 16 muestra $99{,}7\pm0{,}1\,^{\circ}\mathrm C$ a partir de $\bar T=99{,}76247\,^{\circ}\mathrm C$ y $\delta T=0{,}15741\,^{\circ}\mathrm C$. Ese resultado **no coincide** con el redondeo convencional a una cifra significativa de incertidumbre explicado en la Clase 2 (que daría aproximadamente $99{,}8\pm0{,}2\,^{\circ}\mathrm C$). Queda señalada esta discrepancia de los materiales para consultarla si el profesor exige seguir su ejemplo literal.

### 3.5. Propagación: deducción con Taylor (diapositiva 22)

Sea una magnitud calculada $f=f(x,y)$, evaluada cerca de $(x_0,y_0)$. Si las mediciones cambian ligeramente, la expansión de Taylor de primer orden da:

$$
\begin{aligned}
f(x_0+\Delta x,y_0+\Delta y)\approx {}&f(x_0,y_0)\\
&+\left.\frac{\partial f}{\partial x}\right|_0\Delta x
+\left.\frac{\partial f}{\partial y}\right|_0\Delta y.
\end{aligned}
$$

Las derivadas parciales miden la **sensibilidad de $f$** a cada variable. Para estimar conservadoramente la magnitud de la variación, sumamos los valores absolutos:

$$
\boxed{\delta f_{\mathrm{lin}}\approx
\left|\frac{\partial f}{\partial x}\right|\delta x+
\left|\frac{\partial f}{\partial y}\right|\delta y}.
$$

**Método lineal (diapositiva 22):** sumar las contribuciones absolutas de primer orden; útil como estimación conservadora cuando las $\delta x$ y $\delta y$ se interpretan como cotas.

**Método cuadrático (diapositiva 24), para variables independientes y sin correlación:**

$$
\boxed{\delta f_{\mathrm{cuad}}\approx
\sqrt{\left(\frac{\partial f}{\partial x}\delta x\right)^2+
\left(\frac{\partial f}{\partial y}\delta y\right)^2}}.
$$

En esta segunda fórmula, las $\delta x$ y $\delta y$ se interpretan como incertidumbres estándar, no necesariamente como límites máximos.

**Ejemplo que resolvimos (área de un rectángulo):**

$$
a=(2{,}0\pm0{,}1)\,\mathrm m,
\qquad b=(3{,}0\pm0{,}2)\,\mathrm m,
\qquad A=ab.
$$

Como $\partial A/\partial a=b$ y $\partial A/\partial b=a$:

$$
A=6{,}0\,\mathrm{m^2},\qquad
\delta A_{\mathrm{lin}}=0{,}7\,\mathrm{m^2},\qquad
\delta A_{\mathrm{cuad}}=0{,}5\,\mathrm{m^2}.
$$

Es importante **declarar el método usado**, porque describe interpretaciones distintas de la incertidumbre.

### 3.6. Casos particulares del método lineal (diapositiva 23)

Para $\delta x,\delta y\geq0$, y cuando los denominadores no son cero:

| Función    | Incertidumbre lineal                    |          |           |     |                 |
| ---------- | --------------------------------------- | -------- | --------- | --- | --------------- |
| $f=x\pm y$ | $\delta f=\delta x+\delta y$            |          |           |     |                 |
| $f=xy$     | $\delta f=                              | y        | \delta x+ | x   | \delta y$       |
| $f=x/y$    | $\displaystyle\delta f=\frac{\delta x}{ | y        | }+\frac{  | x   | }{y^2}\delta y$ |
| $f=x^n$    | $\delta f=                              | nx^{n-1} | \delta x$ |     |                 |

**Formas relativas**, deducibles al dividir las expresiones anteriores por $|f|$:

$$
\boxed{\text{Producto o cociente:}\quad
\frac{\delta f}{|f|}=\frac{\delta x}{|x|}+\frac{\delta y}{|y|}}
$$

$$
\boxed{\text{Potencia:}\quad
\frac{\delta f}{|f|}=|n|\frac{\delta x}{|x|}}.
$$

> [!tip] Procedimiento reutilizable
> 1. Identificar la función y sus variables medidas.  
> 2. Calcular el valor central en unidades coherentes.  
> 3. Obtener las derivadas parciales.  
> 4. Elegir y **declarar** propagación lineal o cuadrática según el problema.  
> 5. Sustituir incertidumbres, comprobar unidades y redondear **al final**.

## 4. Interpretación y comprobaciones

- **Media vs. dispersión:** dos series pueden tener la misma $\bar{x}$ y distinta $\sigma$.
- **Precisión vs. exactitud:** una $\sigma$ pequeña no demuestra que no exista un sesgo sistemático ([[Clase 2 - Errores experimentales y cifras significativas]]).
- **Unidades:** $[\sigma^2]=[x]^2$, $[\sigma]=[\delta\bar{x}]=[x]$ y $[\delta f]=[f]$.
- **Casos límite:** si todas las mediciones son iguales, $\sigma=0$ para esa serie; esto no garantiza error instrumental ni sistemático nulos.
- **Número de datos:** al aumentar $N$, el error estándar disminuye como $1/\sqrt N$ si la dispersión característica se mantiene estable.
- **Sensibilidad de la función:** una derivada parcial grande puede amplificar el aporte de una incertidumbre instrumental pequeña.
- **Orden de operaciones:** no confundir $\sqrt{\sigma^2}$ con la distancia entre valores consecutivos, ni $\sigma/\sqrt N$ con $\sigma/N$.
- **Distribuciones (diapositivas 17–20):** los histogramas y el ejemplo de ajuste gaussiano ilustran la forma de los datos; aquí no desarrollamos el método de ajuste gaussiano, que queda como profundización.

## 5. En mis palabras

> [!note] Completar mañana sin mirar
> 1. ¿Por qué la media, la desviación estándar y el error estándar responden preguntas diferentes?  
> 2. ¿Por qué aparecen derivadas parciales cuando queremos conocer la incertidumbre de una función?  
> 3. ¿En qué se diferencia interpretar una incertidumbre como cota de variación de interpretarla como incertidumbre estándar?

## 6. Qué debo poder reconstruir sin consultar

- [ ] Explicar cuándo la mediana es más representativa que la media.
- [ ] Deducir por qué se elevan al cuadrado los residuos en la varianza.
- [ ] Calcular $\sigma^2$ y $\sigma$ distinguiendo sus unidades.
- [ ] Explicar por qué $\delta\bar{x}=\sigma/\sqrt N$ y no $\sigma/N$.
- [ ] Aplicar Taylor de primer orden para obtener la fórmula lineal de propagación.
- [ ] Distinguir los supuestos del método lineal y del cuadrático.
- [ ] Deducir las formas relativas del producto, cociente y potencia sin consultar una tabla.
- [ ] Reportar el resultado final con incertidumbre y unidades.

## 7. Recuperación activa — ejercicios para mañana

> [!question] Ejercicio pendiente de la conversación: densidad (**no resuelto**)
> Se midió una masa y un volumen:  
> $$m=(20{,}0\pm0{,}2)\,\mathrm g,\qquad V=(5{,}0\pm0{,}1)\,\mathrm{cm^3}.$$  
> Para $\rho=m/V$, utilizando **propagación lineal**:  
> 1. Calcula $\rho$ con sus unidades.  
> 2. Calcula $\delta\rho/|\rho|$.  
> 3. Calcula $\delta\rho$ en unidades de densidad.  
> 4. ¿Cuál de las dos mediciones contribuye más a la incertidumbre relativa? Justifica.  
> 5. **Después de intentarlo:** repite con propagación cuadrática, suponiendo independencia, y compara.

- [ ] Intenté el problema de densidad completo antes de consultar la solución.
- [ ] Justifiqué los métodos y verifiqué las unidades.

> [!question] Pregunta conceptual
> Si cuadruplicas el número de mediciones independientes y la dispersión del proceso se mantiene estable, ¿qué sucede con $\sigma$ y con $\delta\bar{x}$? ¿Qué ocurriría con un sesgo sistemático constante?

> [!question] Deducción breve
> Sin mirar el apartado 3.6, parte de $f=x/y$: calcula $\partial f/\partial x$ y $\partial f/\partial y$ y reconstruye la incertidumbre relativa **lineal**. ¿Por qué las contribuciones se suman aunque la derivada respecto de $y$ sea negativa?

## 8. Conexiones y dudas

- **Conexiones:** [[Clase 1 - Graficos experimentales]] (histogramas y barras de error); [[Clase 2 - Errores experimentales y cifras significativas]] (errores sistemáticos/aleatorios, cifras significativas); tratamiento de datos del laboratorio del resorte.
- **Fuente de la clase:** `Clase 3_Medidas estadísticas.pdf`, principalmente diapositivas 2–16 y 22–24.
- **Pendiente:** ejercicio de densidad; revisar con el profesor la discrepancia de redondeo de la diapositiva 16, si es relevante para una evaluación.
- **Dudas personales:**

## 9. Tarjetas Anki Bridge

¿Qué diferencia hay entre la media y la mediana de una serie experimental? ⇢%%oab:basic:v1%%La media promedia todos los valores; la mediana es el centro de los datos ordenados y suele ser menos sensible a extremos.

¿Por qué se elevan al cuadrado los residuos al calcular la varianza? ⇢%%oab:basic:v1%%Porque las desviaciones positivas y negativas se cancelan al sumarlas directamente; sus cuadrados cuantifican dispersión.

¿Qué unidades tiene la varianza de mediciones expresadas en metros? ⇢%%oab:basic:v1%%Metros cuadrados (m²); la desviación estándar recupera los metros al tomar la raíz.

¿Qué diferencia hay entre desviación estándar y error estándar del promedio? ⇢%%oab:basic:v1%%La desviación estándar describe dispersión individual; el error estándar caracteriza la incertidumbre estadística de la media.

¿De qué forma depende el error estándar de N mediciones independientes con dispersión estable? ⇢%%oab:basic:v1%%Disminuye como 1/√N; al cuadruplicar N se reduce a la mitad.

¿Por qué aparecen derivadas parciales en la propagación de incertidumbres? ⇢%%oab:basic:v1%%Miden cuánto cambia la función frente a una variación pequeña de cada variable medida, manteniendo las demás fijas.

¿Cuándo se aplica la propagación cuadrática de incertidumbres de la Clase 3? ⇢%%oab:basic:v1%%Para combinar incertidumbres estándar de variables independientes/no correlacionadas, usando las derivadas parciales al cuadrado.

¿Qué caracteriza la propagación lineal de incertidumbres presentada en la Clase 3? ⇢%%oab:basic:v1%%Suma las magnitudes de las contribuciones de primer orden; sirve como estimación conservadora de variación.

¿Cómo se combinan las incertidumbres relativas lineales en un producto o cociente de variables no nulas? ⇢%%oab:basic:v1%%Se suman las incertidumbres relativas de los factores, usando magnitudes absolutas.

¿Cómo afecta una potencia x^n a la incertidumbre relativa lineal, si x≠0? ⇢%%oab:basic:v1%%Se multiplica aproximadamente por |n|: δf/|f| = |n| δx/|x|.
