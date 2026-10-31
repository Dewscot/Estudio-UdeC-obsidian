---
tags:
  - problema
  - calculo-iv
  - funciones-complejas
tipo: problema
asignatura: "Cálculo IV"
unidad: "Semana 2 — Imágenes de conjuntos"
estado: pendiente
fuente: "Apunte del profesor: Semana 2.pdf, pp. 8-9"
dificultad: intermedia
---

> [!question] ¿Qué se pide?
> Hallar la imagen geométrica de la recta $L_a=\{z:\operatorname{Re}z=a\}$, con $a\in\mathbb R\setminus\{0\}$, bajo $f(z)=1/z$.

## 1. Enunciado, datos y condiciones

- **Referencia:** ejemplo de inversión del apunte de Semana 2.
- **Datos:** $z=x+iy$, $x=a\neq0$ y $w=f(z)=\alpha+i\beta$.
- **Incógnitas:** ecuación de $f(L_a)$, centro, radio y puntos excluidos.
- **Restricciones:** $z\neq0$; la recta tiene $y\in\mathbb R$.

## 2. Esquema o representación (si aporta)

Dibuja en el plano $z$ una recta vertical $x=a$ y, en otro plano, la figura que esperas obtener. Señala dónde debería quedar la imagen de los puntos muy lejanos de la recta.

## 3. Principios y herramientas que usaré

- Forma cartesiana: $1/z=(x-iy)/(x^2+y^2)$.
- Imagen de un conjunto: $f(L_a)=\{f(a+iy):y\in\mathbb R\}$.
- Completar cuadrados en la ecuación resultante.
- **Notas relacionadas:** [[Funciones complejas e imágenes de conjuntos]], [[Números complejos, operaciones y módulo]].

## 4. Plan de resolución

1. Escribir $w=1/(a+iy)$ y obtener $\alpha,\beta$.
2. Eliminar el parámetro $y$ o utilizar la identidad $z=1/w$.
3. Reconocer la curva, verificar el origen y revisar el signo de $a$.

## 5. Mi desarrollo

> [!todo] Intento sin consultar
> Escribe aquí tu eliminación del parámetro y el croquis de la imagen.

$$
\alpha=\underline{\qquad\qquad},\qquad
\beta=\underline{\qquad\qquad}.
$$

## 6. Comprobaciones e interpretación

- [ ] Verifiqué que el radio es positivo incluso cuando $a<0$.
- [ ] Revisé si $w=0$ puede alcanzarse con algún $z$ finito.
- [ ] Comprobé un valor concreto, por ejemplo $z=a$.
- [ ] Entiendo qué pasa cuando $y\to\pm\infty$.

> [!example]- Solución de referencia (consultar después del intento)
> Como $z=1/w$, imponer $\operatorname{Re}(1/w)=a$ da $\alpha/(\alpha^2+\beta^2)=a$ para $w\neq0$. Por tanto $\alpha^2+\beta^2=\alpha/a$ y
> $$
> \boxed{\left(\alpha-\frac1{2a}\right)^2+\beta^2=\frac1{4a^2}}.
> $$
> La imagen es la circunferencia de centro $1/(2a)$ y radio $1/(2|a|)$, **sin el origen**. El origen solo se aproxima cuando $|y|\to\infty$.

## 7. Método reutilizable

Para estudiar imágenes bajo $w=1/z$, suele convenir despejar $z=1/w$ e imponer en las coordenadas de $w$ la ecuación del conjunto original.

## 8. Dudas y errores detectados

Registrar aquí si confundí el círculo con el disco, si incluí $w=0$ o si omití el valor absoluto del radio.

## 9. Anki Bridge (opcional)

No se añaden tarjetas: la derivación completa se recupera activamente en esta nota; los conceptos breves ya figuran en [[Funciones complejas e imágenes de conjuntos]].
