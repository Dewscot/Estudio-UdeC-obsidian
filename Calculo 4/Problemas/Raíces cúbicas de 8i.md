---
tags:
  - problema
  - calculo-iv
  - funciones-complejas
tipo: problema
asignatura: "Cálculo IV"
unidad: "Semana 3 — Raíces complejas"
estado: pendiente
fuente: "Ejercicio de práctica basado en: Exponencial, logaritmo, raíces y funciones trig.pdf"
dificultad: inicial
---

> [!question] ¿Qué se pide?
> Encontrar **todas** las soluciones complejas de $w^3=8i$, ubicarlas geométricamente e identificar la raíz principal según la convención del apunte.

## 1. Enunciado, datos y condiciones

- **Datos:** $z=8i$, $n=3$, $w^3=z$.
- **Incógnitas:** tres raíces distintas, sus módulos y argumentos.
- **Condiciones:** $z\neq0$; el argumento principal de $8i$ es $\pi/2$.
- **Fuente:** ejercicio de elaboración propia para practicar el método de la Semana 3.

## 2. Esquema o representación (si aporta)

Dibuja una circunferencia centrada en $0$ del radio que calcules. Marca tres puntos con separaciones angulares iguales.

## 3. Principios y herramientas que usaré

- $w_k=r^{1/n}e^{i(\theta+2\pi k)/n}$, $k=0,\ldots,n-1$.
- Módulos y argumentos; rama principal en el plano cortado.
- **Notas relacionadas:** [[Raíces complejas y ramas]], [[Forma polar, argumento y potencias]].

## 4. Plan de resolución

1. Expresar $8i$ en polar.
2. Igualar módulos y argumentos en $w^3=8i$.
3. Elegir tres valores consecutivos de $k$ y comprobar las soluciones.

## 5. Mi desarrollo

> [!todo] Intento sin consultar
> Registra aquí los tres valores de $w_k$, preferiblemente en forma exponencial, y un croquis.

$$
w_k=\underline{\qquad\qquad\qquad},\quad k=0,1,2.
$$

## 6. Comprobaciones e interpretación

- [ ] Las tres raíces tienen igual módulo.
- [ ] Los argumentos están separados por $2\pi/3$.
- [ ] Elevé cada raíz al cubo y recuperé $8i$.
- [ ] Distinguí «todas las raíces» de «rama principal».

> [!example]- Solución de referencia (consultar después del intento)
> $8i=8e^{i\pi/2}$, de modo que $|w|=2$ y $\arg w=(\pi/2+2\pi k)/3$. Las raíces son
> $$
> \boxed{w_0=2e^{i\pi/6},\quad w_1=2e^{i5\pi/6},\quad w_2=2e^{i3\pi/2}}.
> $$
> Sus ángulos son $\pi/6$, $5\pi/6$ y $3\pi/2$, separados por $2\pi/3$; la rama principal selecciona $w_0$ para $8i$.

## 7. Método reutilizable

Para $w^n=z\neq0$: hallar el módulo $|z|^{1/n}$, dividir los argumentos $\theta+2\pi k$ por $n$ y tomar exactamente $n$ soluciones distintas.

## 8. Dudas y errores detectados

¿Confundí el número de raíces con el orden de la potencia? ¿Usé los argumentos en grados o radianes de forma inconsistente?

## 9. Anki Bridge (opcional)

No se añaden tarjetas: el procedimiento completo conviene reconstruirlo; ver las tarjetas de [[Raíces complejas y ramas]].
