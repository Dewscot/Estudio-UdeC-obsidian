---
tags:
  - electromagnetismo-ii
  - certamen-2
  - inductancia
  - energia-magnetica
estado: estudiado
fuente: "Contenido 4.1 510238 - Inductancia_EnergíaB, diapositivas 15–18"
---

> [!abstract] Pregunta física
> ¿Dónde se almacena la energía de un inductor ideal y por qué depende del cuadrado de la corriente?

## 1. Idea física

Una fuente debe entregar energía para aumentar la corriente en una bobina: la autoinducción se opone a esa variación. En un inductor ideal, la energía suministrada se almacena en su **campo magnético**, no se disipa como calor.

- Una corriente **constante y no nula** mantiene un campo magnético y una energía magnética no nulos.
- Si $di/dt=0$, la fem autoinducida es cero, **pero no necesariamente la energía**.
- Mientras aumenta la **magnitud** de la corriente, aumenta la energía magnética.

## 2. Leyes, hipótesis y convenciones

- **Relación constitutiva:** $v_L=L\,di/dt$ (convención pasiva: $i$ entra por el terminal de potencial positivo).
- **Potencia eléctrica recibida:** $p_L=v_L i$.
- **Fem autoinducida:** $\mathcal E_{\mathrm{ind}}=-L\,di/dt$; no confundir su signo con la tensión pasiva $v_L$.
- **Modelo:** inductor ideal, lineal, de inductancia constante $L>0$, sin pérdidas resistivas.

## 3. Desarrollo matemático

La potencia instantánea que recibe el inductor es

$$
p_L=v_L i=Li\frac{di}{dt}=\frac{dU_B}{dt}.
$$

Por la regla de la cadena (o por cambio de variable al integrar en $t$),

$$
dU_B=Li\,di.
$$

Integrando desde corriente nula y energía magnética nula hasta una corriente $i$:

$$
\int_0^{U_B}dU=L\int_0^i i'\,di'
\quad\Longrightarrow\quad
\boxed{U_B=\frac12 Li^2}.
$$

> [!tip] ¿Por qué aparece el cuadrado?
> El trabajo incremental para aumentar la corriente en $di$ es $dU_B=Li\,di$. Para el mismo incremento de corriente, se necesita más energía cuando $|i|$ ya es mayor.

### Densidad de energía magnética (solenoide largo ideal en vacío)

Para un solenoide de $N$ espiras, sección $A$ y longitud $\ell$:

$$
L=\mu_0\frac{N^2A}{\ell},\qquad B=\mu_0\frac{N}{\ell}i.
$$

Al sustituir ambas relaciones en $U_B=\tfrac12 Li^2$:

$$
U_B=\frac{B^2}{2\mu_0}A\ell.
$$

Como $A\ell$ es el volumen aproximado ocupado por el campo, obtenemos:

$$
\boxed{u_B=\frac{U_B}{A\ell}=\frac{B^2}{2\mu_0}}.
$$

Este resultado se extiende al campo magnético en el vacío: $u_B=B^2/(2\mu_0)$. La deducción anterior utiliza el solenoide ideal como modelo sencillo.

## 4. Interpretación y comprobaciones

- **Unidades:** $[Li^2]=\mathrm{H}\,\mathrm{A}^2=\mathrm{J}$; $[u_B]=\mathrm{J/m^3}$.
- **Caso constante:** $i\ne0$ y $di/dt=0$ implica $U_B>0$ y $\mathcal E_{\mathrm{ind}}=0$.
- **Duplicar la corriente:** a $L$ fija, $U_B(2i)=4U_B(i)$; la variación es $\Delta U_B=3U_B(i)$.
- **Campo y geometría:** para un solenoide ideal, duplicar $i$ duplica $B$ pero **no** altera $L$.
- **Sin resistencia:** el inductor no disipa potencia promedio por efecto Joule; puede recibir y devolver energía.

## 5. En mis palabras

> [!note] Explicación personal
> Sin consultar: ¿cómo explicarías que una bobina con corriente constante tiene energía aunque su fem autoinducida sea cero?

## 6. Qué debo poder deducir sin consultar

- [ ] Obtener $U_B=\tfrac12 Li^2$ desde $p_L=v_Li$.
- [ ] Explicar por qué la fem depende de $di/dt$ y la energía depende de $i^2$.
- [ ] Deducir $u_B=B^2/(2\mu_0)$ para un solenoide ideal en vacío.
- [ ] Interpretar el efecto de duplicar $i$, sin confundirlo con duplicar $L$.

## 7. Recuperación activa

1. **Conceptual:** ¿pueden ser simultáneamente $\mathcal E_{\mathrm{ind}}=0$ y $U_B>0$? Da un caso.
2. **Deducción:** partiendo de $p_L=Li\,di/dt$, reconstruye la expresión de $U_B$ sin mirar.
3. **Aplicación breve:** si $i_f=2i_0$, calcula $U_f/U_i$ y $\Delta U$.

## 8. Conexiones y dudas

- **Se relaciona con:** [[Autoinducción e inductancia]] · [[Oscilaciones LC]].
- **Dudas pendientes:** anotar aquí interpretaciones que necesiten repasarse.

---
**Fuente principal:** presentación del profesor, *Contenido 4.1 — Inductancia y Energía B*, diapositivas 15–18. La separación de variables, las verificaciones y las preguntas están formuladas como apoyo de estudio.

<!-- INICIO TARJETAS ANKI BRIDGE C2 (agregadas sin modificar teoría) -->

### Tarjetas para Anki Bridge — Energía magnética

¿Qué representa $u_B$ y cuánto vale para un campo magnético en el vacío? ⇢%%oab:basic:v1%%Es la energía magnética por unidad de volumen: $u_B=B^2/(2\mu_0)$. Puede deducirse para un solenoide ideal usando $U_B=Li^2/2$.

Si $i<0$ pero $di/dt>0$ en un inductor ideal, ¿aumenta o disminuye su energía magnética? ⇢%%oab:basic:v1%%Disminuye: $dU_B/dt=Li\,di/dt<0$. La corriente negativa se aproxima a cero, por lo que disminuye $|i|$.

¿Cómo se deduce la energía de un inductor ideal de inductancia constante desde la potencia eléctrica recibida? ⇢%%oab:basic:v1%%Con la convención pasiva, $P=v_Li=Li,di/dt=dU_B/dt$. Entonces $dU_B=Li,di$ y al integrar desde $i=0$ se obtiene $U_B=\frac12 Li^2$.

Si se duplica la corriente de un inductor ideal manteniendo constante $L$, ¿cómo cambian la energía final y su incremento? ⇢%%oab:basic:v1%%Como $U_B=\frac12 Li^2$, la energía final es $4U_{Bi}$ y el incremento es $\Delta U_B=3U_{Bi}$. La inductancia no cambia al variar la corriente en un modelo lineal.

<!-- FIN TARJETAS ANKI BRIDGE C2 -->

