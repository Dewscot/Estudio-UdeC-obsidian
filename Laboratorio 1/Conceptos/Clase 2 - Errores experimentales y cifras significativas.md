---
tags:
  - laboratorio-1
  - conceptos
  - errores-experimentales
estado: repasar
fuente: "Clase 2_Errores.pdf (diapositivas 1-28); Clase 2 - ejemplo errores.pdf"
---

# Clase 2 — Errores experimentales y cifras significativas

> [!abstract] Pregunta física
> ¿Cómo distinguir las distintas fuentes de error de una medición y reportar un resultado con una incertidumbre y una precisión numérica coherentes?

## 1. Idea física

Toda medición está limitada por el instrumento, el procedimiento y las condiciones de observación. Una serie de mediciones puede ser muy **reproducible** y, sin embargo, estar desplazada respecto al valor verdadero. La clase distingue tres cualidades (diapositivas 3-8):

| Concepto | Qué evalúa |
|---|---|
| **Exactitud** | Cercanía entre el resultado experimental y el valor verdadero o de referencia. |
| **Precisión** | Concordancia entre mediciones repetidas en condiciones similares. |
| **Sensibilidad** | Capacidad del instrumento para apreciar cambios pequeños en la magnitud medida. |

**Ejemplo:** mediciones de $105{,}0$ g repetidas casi sin dispersión para un objeto de valor de referencia $100{,}0$ g: alta precisión, baja exactitud. Un instrumento con divisiones muy finas puede ser sensible y estar mal calibrado.

## 2. Leyes, hipótesis y convenciones

### 2.1. Tipos de error (diapositivas 9-15)

- **Sistemático:** afecta las mediciones de forma reproducible o predecible. Puede surgir del instrumento (calibración), del observador (paralaje reiterado) o del método elegido. Suele introducir **sesgo** y comprometer la exactitud.
- **Aleatorio:** se manifiesta como variaciones no reproducibles de una medición a otra, aun en condiciones similares. Produce **dispersión** y compromete la precisión; puede estudiarse estadísticamente.

> [!warning] Distinción fundamental
> Promediar mediciones puede reducir la incertidumbre estadística asociada a fluctuaciones aleatorias, pero **no corrige por sí solo un sesgo sistemático**. El nombre de una causa (p. ej., paralaje) no decide automáticamente la clasificación: importa cómo se comporta.

### 2.2. Incertidumbre del instrumento (diapositiva 16)

La convención **enseñada en esta presentación** es

$$
\boxed{\Delta x_{\mathrm{aparato}}=\frac{s}{2}},
$$

con $s$ como sensibilidad o división mínima de la escala. Por ejemplo, una regla graduada de milímetro en milímetro lleva a una estimación de $\Delta x_{\mathrm{aparato}}=0{,}5\,\mathrm{mm}$.

**Alcance:** es una convención del curso para los instrumentos considerados; no debe aplicarse automáticamente a todos los instrumentos digitales. La diapositiva 19 indica, para el procedimiento presentado, tomar el mayor entre el error del medidor y el del aparato.

### 2.3. Forma de informar un resultado (diapositivas 18 y 26-28)

$$
\boxed{x=(x_{\mathrm{medido}}\pm\Delta x)\,[\text{unidad}]}.
$$

La incertidumbre acompaña a la medida: reportar solamente el valor numérico omite información acerca de su calidad.

## 3. Desarrollo matemático

### 3.1. Error absoluto, relativo y porcentual (diapositivas 19-20)

Si existe un valor verdadero o de referencia $X_{\mathrm{ref}}$, podemos calcular el error absoluto de un valor experimental $X_{\mathrm{exp}}$:

$$
\varepsilon_a=|X_{\mathrm{ref}}-X_{\mathrm{exp}}|.
$$

Tiene las mismas **unidades** que la magnitud medida. Siguiendo el denominador **usado por la presentación**:

$$
\varepsilon_r=\frac{\varepsilon_a}{|X_{\mathrm{exp}}|},
\qquad
\varepsilon_{\%}=100\,\varepsilon_r\,\%.
$$

El relativo es adimensional; el porcentual expresa su proporción en porcentaje (si $X_{\mathrm{exp}}\neq0$).

**Ejemplo propio para practicar la convención:** $X_{\mathrm{ref}}=20{,}0\,\mathrm{cm}$ y $X_{\mathrm{exp}}=19{,}5\,\mathrm{cm}$.

$$
\varepsilon_a=0{,}5\,\mathrm{cm},\qquad
\varepsilon_r=\frac{0{,}5}{19{,}5}\simeq0{,}0256,
\qquad \varepsilon_{\%}\simeq2{,}56\%.
$$

> [!note] Error no es lo mismo que incertidumbre
> El **error** compara con un valor verdadero o de referencia; la **incertidumbre** cuantifica la duda asignada al resultado. Si no conocemos el valor verdadero, la diapositiva 19 propone usar el promedio como referencia práctica, pero este no se vuelve por ello el valor verdadero.

### 3.2. Cifras significativas y redondeo (diapositivas 21-28)

La presentación pide **reportar la incertidumbre con una cifra significativa** y redondear la medición **hasta la misma posición decimal**.

**Ejemplo del documento de ejercicios:**

$$
12{,}3456\pm0{,}0234\,\mathrm g
\quad\longrightarrow\quad
\boxed{(12{,}35\pm0{,}02)\,\mathrm g}.
$$

Pasos:

1. Redondear la incertidumbre: $0{,}0234\rightarrow0{,}02$ g.
2. Identificar su última posición significativa: **centésimas** de gramo.
3. Redondear el valor medido a esa posición: $12{,}3456\rightarrow12{,}35$ g.

**Reglas sobre ceros:** los ceros antes del primer dígito no nulo no son significativos; los ceros entre dígitos no nulos sí lo son; los ceros finales a la derecha de una coma decimal pueden expresar precisión y sí son significativos (ejemplo de clase: $45{,}500$).

> [!important] No redondear demasiado pronto
> Conserva suficientes dígitos durante los cálculos y redondea al **reportar el resultado** para no acumular errores de redondeo.

## 4. Interpretación y comprobaciones

- **Unidades:** $\varepsilon_a$ tiene unidades; $\varepsilon_r$ es adimensional; $\varepsilon_{\%}$ es un porcentaje.
- **Instrumento:** identifica si la resolución indicada es una división de escala, una especificación digital o una incertidumbre entregada por fabricante.
- **Exactitud frente a precisión:** una dispersión muy pequeña no prueba ausencia de sesgo.
- **Notación:** valor e incertidumbre deben terminar en la misma posición decimal; no omitir unidades.
- **Clasificación:** preguntar si el efecto desplaza las lecturas persistentemente o introduce variaciones impredecibles.

## 5. En mis palabras

> [!note] Explicación personal (completar sin mirar)
> Explica con un ejemplo inventado por ti por qué repetir una medición no necesariamente mejora su exactitud. ¿Cómo distinguirías sensibilidad instrumental de precisión experimental?

## 6. Qué debo poder deducir sin consultar

- [ ] Diferenciar exactitud, precisión y sensibilidad con un ejemplo para cada una.
- [ ] Clasificar una fuente de error y **justificarla por su comportamiento**.
- [ ] Estimar $\Delta x_{\mathrm{aparato}}$ con la convención de las diapositivas, cuando corresponda.
- [ ] Calcular $\varepsilon_a$, $\varepsilon_r$ y $\varepsilon_\%$ comprobando unidades.
- [ ] Reportar $x\pm\Delta x$ con cifras significativas coherentes.

## 7. Recuperación activa

1. **Conceptual:** una balanza marca siempre $0{,}05$ g de más. ¿Qué tipo de error predomina y por qué no desaparece al promediar?
2. **Caso ambiguo:** el paralaje de una probeta puede generar error sistemático o aleatorio. Describe una situación para cada caso.
3. **Cálculo breve:** expresa correctamente $(15{,}345\pm0{,}087)\,\mathrm{cm}$ usando la convención del profesor.
4. **Comprobación:** si $X_{\mathrm{ref}}=50{,}0\,\mathrm s$ y $X_{\mathrm{exp}}=49{,}0\,\mathrm s$, calcula los tres errores e indica unidades.

## 8. Conexiones y dudas

- **Se relaciona con:** [[Clase 1 - Graficos experimentales]] (barras de error); clase 3 (promedio, dispersión y propagación); reporte del laboratorio del resorte (paralaje y referencia inicial).
- **Materiales:** `Clase 2_Errores.pdf` (principal) y `Clase 2 - ejemplo errores.pdf` (ejercicios de redondeo y clasificación).
- **Dudas pendientes:**

## 9. Tarjetas Anki Bridge

¿Qué diferencia hay entre exactitud y precisión en mediciones repetidas? ⇢%%oab:basic:v1%%Exactitud: cercanía al valor de referencia. Precisión: cercanía entre las mediciones repetidas.

¿Qué significa sensibilidad de un instrumento de medición? ⇢%%oab:basic:v1%%Capacidad para distinguir cambios pequeños en la magnitud medida.

¿Cómo se reconoce un error sistemático? ⇢%%oab:basic:v1%%Provoca una desviación reproducible o predecible, como un sesgo de calibración.

¿Cómo se reconoce un error aleatorio? ⇢%%oab:basic:v1%%Produce fluctuaciones impredecibles entre mediciones realizadas en condiciones similares.

¿Por qué un promedio no corrige un error sistemático constante? ⇢%%oab:basic:v1%%Porque el sesgo se mantiene en cada medición y también en su promedio.

¿Qué incertidumbre instrumental propone la clase para una escala de división mínima s? ⇢%%oab:basic:v1%%La mitad de la división: Δx = s/2, según la convención de esta clase.

¿Qué diferencia al error absoluto del relativo? ⇢%%oab:basic:v1%%El absoluto tiene unidades de la magnitud; el relativo es el absoluto dividido por el valor medido y no tiene unidades.

¿Qué criterio se usa para redondear una medición y su incertidumbre en esta clase? ⇢%%oab:basic:v1%%Incertidumbre a una cifra significativa y medida hasta la misma posición decimal.
