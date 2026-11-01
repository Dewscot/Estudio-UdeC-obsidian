# Criterios para integrar funciones complejas

> [!important] Idea central
> **Elegir el método según sus hipótesis, no por la apariencia del integrando.** Primero identifica los puntos problemáticos y su posición respecto al contorno.

## 1. Antes de integrar

1. Determinar dónde es holomorfo el **integrando completo**.
2. Localizar los puntos problemáticos respecto de la curva: **interior, exterior o sobre el contorno**.
3. Comprobar si hay una **primitiva válida en un abierto que contiene toda la curva**.
4. Comprobar las hipótesis de Cauchy–Goursat (CG) o de la fórmula integral de Cauchy (FIC).
5. Si corresponde, usar fracciones parciales o parametrización directa.

**Advertencia:** holomorfía *sobre la curva* no es lo mismo que holomorfía *en la curva y en todo su interior*.

## 2. Teorema fundamental de las integrales complejas

Si $F'=f$ en un abierto que contiene toda una curva regular a trozos $\gamma:[a,b]\to\mathbb C$, entonces

$$
\int_\gamma f(z)\,dz=F(\gamma(b))-F(\gamma(a)).
$$

Para una curva cerrada, los extremos coinciden y la integral es **cero**.

- **Hipótesis decisiva:** encontrar una primitiva *válida sobre toda la curva*, en un abierto que la contenga.
- **No exige**, por sí mismo, que la primitiva esté definida en todo el interior de la curva.
- **No es lo mismo que parametrizar:** la parametrización utiliza $z=z(t)$ y $dz=z'(t)dt$ para calcular directamente la integral.

### Ejemplo: obstáculo para una primitiva global

Para $f(z)=1/(z-1)$ sobre $C:|z-1|=2$ orientada positivamente,

$$
\oint_C\frac{dz}{z-1}=2\pi i\neq 0.
$$

Como la integral cerrada es no nula, **no existe una primitiva global de $1/(z-1)$ en $\mathbb C\setminus\{1\}$**, aunque sí hay primitivas locales dadas por ramas de $\log(z-1)$. Cualquier corte de una rama logarítmica que salga de $z=1$ intersecta esta circunferencia.

## 3. Teorema de Cauchy–Goursat (CG)

En la versión utilizada para una curva simple cerrada $C$, si $f$ es holomorfa en un abierto que contiene **la curva y todo su interior**, entonces

$$
\boxed{\oint_C f(z)\,dz=0.}
$$

- **Hipótesis decisiva:** holomorfía del **integrando completo** en la curva y su interior.
- No necesitamos encontrar una primitiva explícita.
- Si alguna singularidad queda dentro, **no podemos aplicar directamente esta versión** del teorema. Eso **no demuestra** que la integral sea distinta de cero.

**Ejemplo:**

$$
\oint_{|z|=2}\frac{z^2+1}{z-3}\,dz=0,
$$

pues la única singularidad está en $z=3$, fuera de la curva y su interior.

## 4. Fórmula integral de Cauchy (FIC)

Para una curva simple cerrada $C$ orientada positivamente y un punto $a$ **estrictamente interior**,

$$
\boxed{\oint_C\frac{g(z)}{z-a}\,dz=2\pi i\,g(a),}
$$

si $g$ es holomorfa en un abierto que contiene la curva y su interior.

- **Hipótesis decisiva:** la función del numerador $g$ debe ser holomorfa en toda la región relevante, y $a$ debe estar **dentro** de $C$.
- El integrando completo $g(z)/(z-a)$ puede tener una singularidad en $a$: esto **no impide** aplicar la FIC.
- Si $a$ está **fuera**, no debemos sustituir simplemente $g(a)$ en la FIC. En ese caso, puede resultar más directo aplicar CG si el integrando completo es holomorfo en el interior.

**Ejemplo:**

$$
\oint_{|z|=2}\frac{z^2+2}{z-i}\,dz=2\pi i\,(i^2+2)=2\pi i.
$$

**Ejemplo de cancelación:**

$$
\frac{1}{z^2+1}=\frac{-i/2}{z-i}+\frac{i/2}{z+i}.
$$

Sobre $|z|=2$, la FIC aplicada a ambas fracciones da dos contribuciones $\pi$ y $-\pi$. Por ello, la integral total es **cero**, aunque haya dos singularidades interiores.

## 5. Comparación rápida

| Método | ¿Qué debo verificar? | Conclusión |
|---|---|---|
| **Teorema fundamental** | Existe $F'=f$ en un abierto que contiene toda la curva | Diferencia $F(\text{final})-F(\text{inicial})$; en curva cerrada vale $0$ |
| **CG** | El **integrando completo** es holomorfo sobre la curva y en su interior | Integral cerrada igual a $0$ |
| **FIC** | $g$ es holomorfa en la región relevante; $a$ está **dentro**; forma $g(z)/(z-a)$ | $2\pi i\,g(a)$ para orientación positiva |
| **Parametrización directa** | El integrando es continuo a lo largo del camino y este es regular a trozos | Sustituir $z=z(t)$ y $dz=z'(t)\,dt$ |

## 6. Errores detectados durante el estudio

1. **Confundir la función integranda con una primitiva:** que una rama de $\log(z-1)$ falle en un punto del contorno no significa que $1/(z-1)$ falle allí.
2. **Aplicar CG comprobando solo la curva:** para esta versión también hay que examinar el interior.
3. **Aplicar FIC con $a$ exterior:** que $g$ sea un polinomio no es suficiente si $a$ no está dentro.
4. **Concluir que la integral es no nula si CG no sirve:** las contribuciones pueden cancelarse.
5. **Confundir el teorema fundamental con parametrizar:** el primero utiliza una primitiva; el segundo integra la expresión en el parámetro.
6. **Cambiar accidentalmente las vueltas de un contorno:** $z(t)=1+2e^{2it}$, con $0\le t\le 2\pi$, da dos vueltas; $1+2e^{it}$ da una.

## 7. Recuperación activa

Sin consultar lo anterior, justifica:

1. ¿Por qué una primitiva sobre toda la curva permite asegurar integral cero cuando el camino es cerrado?
2. ¿Por qué el integrando de la FIC no tiene que ser holomorfo en $a$, pero $g$ sí?
3. Si una función tiene singularidades interiores, ¿por qué CG no decide por sí solo el valor de la integral?
4. ¿Por qué no se puede usar FIC en $\oint_{|z|=2}(z^2+1)/(z-3)\,dz$?

## 8. Tarjetas Anki Bridge

¿Cuál es la condición decisiva para aplicar el teorema fundamental de las integrales complejas a una curva cerrada? ⇢%%oab:basic:v1%%Que el integrando tenga una primitiva en un abierto que contenga toda la curva. No es necesario exigir una primitiva en todo su interior.

¿Qué hipótesis garantizan que Cauchy–Goursat anule la integral sobre una curva simple cerrada? ⇢%%oab:basic:v1%%Que el integrando completo sea holomorfo en un abierto que contenga el contorno y todo su interior.

En la fórmula integral de Cauchy, ¿qué condiciones deben cumplir g(z) y el punto a? ⇢%%oab:basic:v1%%g debe ser holomorfa en un abierto que contenga la curva y su interior; a debe estar estrictamente dentro. Con orientación positiva, la integral de g(z)/(z−a) vale 2πi·g(a).

Si una función tiene singularidades interiores y no es aplicable directamente Cauchy–Goursat, ¿qué podemos afirmar del valor de la integral? ⇢%%oab:basic:v1%%No podemos decidir si es cero o distinta de cero solo por ese hecho. Debemos justificar el valor mediante otro método válido.

¿Por qué una integral cerrada no nula impide que exista una primitiva global sobre un dominio que contiene la curva? ⇢%%oab:basic:v1%%Porque, si existiera tal primitiva, el teorema fundamental obligaría a que toda integral cerrada en ese dominio fuera cero.
