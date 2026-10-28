---
tags:
  - laboratorio-1
  - conceptos
  - graficos
estado: repasar
fuente: "Clase 1_Gráficos.pdf (diapositivas 1-19); Clase 1 - ejemplos para graficar a mano.pdf"
---

# Clase 1 — Gráficos experimentales

> [!abstract] Pregunta física
> ¿Cómo representamos datos experimentales para identificar relaciones entre variables y mostrar la incertidumbre de las mediciones sin inducir interpretaciones incorrectas?

## 1. Idea física

Un gráfico facilita **comprender, comparar y analizar** datos relacionados: permite observar tendencias, patrones y relaciones que serían difíciles de identificar en una tabla (diapositivas 2-3).

- **Histograma:** distribuye observaciones cuantitativas entre intervalos; la altura de cada barra representa su frecuencia cuando los intervalos tienen igual anchura. Los intervalos son contiguos.
- **Gráfico XY:** ubica pares de mediciones $(x_i,y_i)$ y permite estudiar una relación funcional entre variables (diapositivas 9-10).
- **Gráficos de barras y circular:** aparecen como ejercicios complementarios de la guía; sirven para comparar categorías y representar partes de un total, respectivamente.

> [!important] Elegir bien la representación
> Varias mediciones de **una misma magnitud** que queremos distribuir → histograma. Dos magnitudes medidas conjuntamente para explorar su relación → gráfico XY. Cantidades por categoría → barras.

## 2. Leyes, hipótesis y convenciones

No se aplica una ley física específica: la clase fija **convenciones de representación** (diapositivas 11-16).

1. Identificar los ejes con la **magnitud y su unidad**.
2. Ubicar, por regla general del curso, la variable **independiente en el eje horizontal** y la **dependiente en el vertical**.
3. Escoger divisiones uniformes, legibles y sencillas (por ejemplo, $1, 2, 5, 10, 20,\ldots$ unidades).
4. Rotular las divisiones de la escala, **no cada valor experimental sobre el eje**.
5. Marcar los datos como puntos experimentales y, si corresponde, acompañarlos de sus **incertidumbres**.

**Convención de los intervalos del histograma:** para no contar una observación dos veces, pueden definirse intervalos como $[30,35)$, $[35,40)$, etc. El ancho de los intervalos modifica el nivel de detalle observado. Esta aclaración amplía el ejercicio de la guía.

## 3. Desarrollo matemático

### 3.1. Rectángulo de error

Una medición de dos variables se escribe como

$$
(x\pm\Delta x,\;y\pm\Delta y).
$$

El punto central es $(x,y)$, mientras que su rectángulo de error abarca

$$
 x-\Delta x\leq x'\leq x+\Delta x,
 \qquad y-\Delta y\leq y'\leq y+\Delta y.
$$

![[Rectangulo de error.svg]]

- Incertidumbre $\Delta x$ despreciable **a la escala del gráfico** → se aprecia principalmente la barra vertical.
- Incertidumbre $\Delta y$ despreciable → se aprecia principalmente la barra horizontal.
- Ambas despreciables gráficamente → parece un punto, **pero eso no significa incertidumbre nula**.

**Ejemplo de la presentación (diapositiva 9):** distancia $(20\pm1)\,\mathrm m$ y tiempo $(0{,}93\pm0{,}05)\,\mathrm s$. Se representa el punto $(20,0{,}93)$ con extensiones horizontales $19$–$21\,\mathrm m$ y verticales $0{,}88$–$0{,}98\,\mathrm s$.

### 3.2. Linealizar un modelo de potencia (diapositivas 17-18)

Para un modelo $y=Cx^{\alpha}$, con $C>0$, $x>0$ e $y>0$:

$$
\log y=\log C+\alpha\log x.
$$

Si definimos $X=\log x$ e $Y=\log y$, obtenemos una recta:

$$
\boxed{Y=\alpha X+\log C}.
$$

La **pendiente** del gráfico log-log es $\alpha$. Para $y=C/x^{\alpha}$, resulta $Y=-\alpha X+\log C$ y la pendiente es $-\alpha$.

### 3.3. Crecimiento exponencial (diapositiva 19)

La diapositiva compara la misma relación de crecimiento exponencial en escala aritmética y **semilogarítmica**. Por ejemplo, para $N(t)=N_0e^{kt}$:

$$
\ln N=\ln N_0+kt.
$$

Por eso es conveniente una **escala lineal en $t$** y **logarítmica en $N$**. No es necesario aplicar logaritmo al tiempo (y $t=0$ no podría mostrarse en un eje temporal logarítmico).

## 4. Interpretación y comprobaciones

- **Significado físico:** las tendencias permiten contrastar relaciones propuestas por un modelo; las barras muestran qué incertidumbre acompaña a cada medición.
- **Unidades:** escribir, por ejemplo, `Tiempo (s)` y `Distancia (m)`; si una pendiente se obtiene en ejes lineales, sus unidades son $[y]/[x]$.
- **Escalas:** una elección poco adecuada puede comprimir o exagerar visualmente diferencias. Verificar si los datos caben y son legibles.
- **Casos límite:** un error gráficamente invisible no equivale a un error exactamente nulo.
- **Logaritmos:** verificar la positividad de las variables a las que se aplica $\log$.

> [!example] Conexión computacional (complementaria)
> En Matplotlib, `plt.errorbar(x, y, xerr=dx, yerr=dy, fmt='o')` representa las incertidumbres; `plt.xscale('log')` y `plt.yscale('log')` cambian las escalas. No reemplazan el razonamiento sobre qué escala elegir.

## 5. En mis palabras

> [!note] Explicación personal (completar sin mirar)
> Explica por qué dos gráficos de los mismos datos pueden favorecer interpretaciones diferentes. ¿Qué información aportan las barras de error que no muestra una nube de puntos por sí sola?

## 6. Qué debo poder deducir sin consultar

- [ ] A partir de $(x\pm\Delta x,y\pm\Delta y)$, construir los límites del rectángulo de error.
- [ ] Obtener la pendiente de un modelo $y=Cx^\alpha$ al representarlo en escala log-log.
- [ ] Justificar cuándo conviene un histograma y cuándo un gráfico XY.
- [ ] Elegir e identificar ejes, escalas y unidades de un experimento.

## 7. Recuperación activa

1. **Conceptual:** si $\Delta x$ es muy pequeña en relación con la escala, ¿qué barra se aprecia y por qué no podemos afirmar que $\Delta x=0$?
2. **Deducción breve:** transforma $y=C/x^2$ en la ecuación de una recta en coordenadas log-log. ¿Cuál es su pendiente?
3. **Aplicación:** si una colonia de bacterias se duplica por hora, ¿qué eje debe estar en escala logarítmica para observar una recta? ¿Qué ocurre si hay una medición en $t=0$?

## 8. Conexiones y dudas

- **Se relaciona con:** [[Clase 2 - Errores experimentales y cifras significativas]]; incertidumbre instrumental, análisis de mediciones repetidas y ajuste de modelos.
- **Materiales:** `Clase 1_Gráficos.pdf` (principal), `Clase 1 - ejemplos para graficar a mano.pdf` (ejercicios).
- **Dudas pendientes:**

## 9. Tarjetas Anki Bridge

¿Por qué usamos gráficos en el análisis experimental? ⇢%%oab:basic:v1%%Para reconocer relaciones, patrones y tendencias y facilitar la comparación de datos.

¿Cuándo conviene un histograma en lugar de un gráfico XY? ⇢%%oab:basic:v1%%Cuando interesa la distribución de frecuencias de una magnitud, no la relación entre dos variables.

¿Qué debe identificar cada eje de un gráfico experimental? ⇢%%oab:basic:v1%%La magnitud física representada y sus unidades.

¿Dónde se ubican normalmente la variable independiente y la dependiente? ⇢%%oab:basic:v1%%La independiente en el eje horizontal y la dependiente en el vertical.

¿Qué representa el rectángulo de error de un punto XY? ⇢%%oab:basic:v1%%Los intervalos desde x−Δx hasta x+Δx y desde y−Δy hasta y+Δy.

¿Una barra de error invisible implica incertidumbre nula? ⇢%%oab:basic:v1%%No. Puede ser demasiado pequeña para apreciarse a la escala utilizada.

¿Qué indica la pendiente de un gráfico log-log de y=Cx^α? ⇢%%oab:basic:v1%%El exponente α, siempre que el modelo de potencia sea aplicable y los logaritmos estén definidos.

¿Qué escala linealiza un crecimiento exponencial de una magnitud positiva en el tiempo? ⇢%%oab:basic:v1%%La semilogarítmica: tiempo lineal y magnitud creciente en eje vertical logarítmico.
