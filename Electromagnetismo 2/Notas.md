



>[!question]-  Si circula una corriente constante y distinta de cero por un solenoide, ¿existe campo magnético? ¿Existe fem autoinducida? Justifica ambas respuestas.
>**Mi respuesta**
>
>Si existe un campo magnético al recorrer corriente el solenoide (justificarlo mas no sé). Dada la condición de corriente constante no debería de existir una fem autoinducida, ya que la fem autoinducida es una fuerza que es contraria al cambio, queriendo mantener la normalidad del sistema

>[!tip]- Correcion
>
>Existe un campo magnético al recorrer corriente el circuito y se puede describir con la Ley de Ampére. No existe fem autoinducida ya que la corriente es constante en el tiempo

>[!question]- Supongamos que la corriente aumenta con el tiempo. ¿Qué sucede con la fem autoinducida si la rapidez de aumento de la corriente se duplica, manteniendo \(L\) constante?
>*Respuesta*
>La fem autoinducida empieza a crear una fuerza contraria al cambio, reduciendo el cambio hasta que vuelve se vuelve a eliminar al terminar el aumento, debería de ser el doble la fem inducida $e=L2$ 

>[!tip]- correcion
>Ya que la  fem autoinducida se define $$ e = -L\frac{di}{dt}$$ al duplicar el aumento de corriente queda $$ e = -L\frac{2di}{dt} \implies e=-2L\frac{di}{dt} $$ por lo que se duplica la fem autoinducida 


>[!question]-  ¿Por qué la inductancia de un solenoide ideal depende de su geometría, mientras que la fem autoinducida depende también de cómo varía la corriente?:
> No sé porque razón depende de su geometría, entiendo que la fem autoinducida viene de $\epsilon = L \frac{di}{dx}$

>[!tip]-  correcion
> la inductancia se define $$ L=\frac{N}{i} \Phi_B$$
> Mientras que el flujo magnético se define $$\int_{s}B\cdot d\vec{A}$$ por lo tanto La inductancia depende 


Si calculamos la inductancia de cada solenoide $$ L_a=u_0\frac{N_a^2 A}{l} \quad   L_b=u_0\frac{N_b^2 A}{l} $$ Y tomamos la relación $$ N_b=2N_a $$ si remplazamos en $L_b$ tendremos que $L_b = u_0\frac{4N_{a}{^2}A}{l}$ el cual si dividimos $\frac{L_b}{L_a}$ tendremos que la inductancia de $L_b$ es 4 veces mayor al tener el doble de espiras que la inductancia $L_a$. Mi 1 1 es que al haber mayor cantidad de espiras en la cual transcurre corriente, producen un campo 1 mayor por lo cual al producir un cambio de corriente, se produce una mayor fuerza contraria al cambio del campo magnético

al duplicar la corriente la $$U_{Bf}=2Li_0^2 \implies \Delta U=Li_0^2 \frac{3}{2}$$ Siendo esa su diferencia de energía. Pero la parte física, al duplicar la corriente lo que está cambiando es la corriente que pasa por cada espira manteniendo la misma geometría el inductor, por lo que la fem autoinducida solo se modifica por la parte de la corriente $e=L2\frac{di}{dt}$ aumentando su valor, pero eso no explica el aumento de 3/2 de energía. Ya que pasa el doble de corriente, el flujo magnético aumenta al pasar más corriente en la misma medida de longitud y, por lo tanto ~~la inductancia aumenta~~ el campo magnético aumenta.
Si duplicamos la corriente, se duplica el campo magnético y, por lo tanto, se duplica el flujo magnético
$u_b \implies$ densidad energética magnética 
$$u_b=\frac{B^2}{2\mu_{0}}$$
Entonces si duplicamos el campo magnético al duplicar la corriente 
$$u_{b}=\frac{(2B)^2}{2\mu}=\frac{2B{^2}_{2}}{\mu}, \quad B=\mu_{0}\frac{N}{l}i,\quad L=\mu_{0}\frac{N^2A}{l}$$ Primero el campo magnético al aumentar la corriente de ${}i_{0}\to 5i_{0}{}$ se multiplica por 5 ${}B_{i}=\mu_{0} \frac{N}{l}i_{0}\to B_{f}=\frac{\mu_{0}N}{l}5i_{0}{}$ siendo 5 veces el valor del campo magnético inicial. Para la ${} \varepsilon{}$ tiene que ser 0, ya que la corriente deja de cambiar al final. Para la energía almacena ${}U_{Bi}=\frac{1}{2}Li^{2}\to U_{Bf}=\frac{1}{2}L(5i_{0})^{2}=\frac{1}{2}L 25i_{0}^{2}{}$ siendo después del cambio de corriente
$$
\Delta U_{B}=\frac{1}{2}L i_{0}^{2}(25-1)=12L i_{0}^{2}
$$
25 veces mayor energía almacenada 

>[!question]- Energia capacitiva y energia magnetica
>$$
 U_{C}=\frac{q^{2}}{2C} \quad U_{B}=\frac{1}{2}L i^{2}
 $$


$$
L \frac{di}{dt}=\frac{Q}{C}, \quad  i=- \frac{dq}{dt} \to \quad -L \frac{d^{2}q}{dt^{2}}=\frac{Q}{C} \to \quad \frac{d^{2}q}{dt^{2}}+ \frac{q}{LC}=0
$$
Una EDO con nuestra convención de corriente, la misma que un oscilador armonico simple 
${}\frac{d^{2}x}{dt^{2}}+\omega^{2}_{0}x=0{}$


No he estudiado el oscilador armónico simple o puede que no me acuerde, pero comparando ambas EDO puedo pensar que ${}\omega_{0}=\frac{1}{\sqrt{ LC }}{}$ lo que aunque lo veremos más tarde, ¿no es el valor de resonancia teórico para circuitos LC o RCL?, sobre las unidades no entiendo muy bien que te refieres. Ahora sobre la EDO, me gustaría resolverla con transformadas de Laplace, ya que creo que a la larga que me aprenda como trabajarlas con álgebra me facilitara con la cantidad de ED que voy a tener que aprender en la carrera, aunque si quieres puedes mostrarme con solución homogénea y particular, solo que no me acuerdo mucho del método.  

Llegue a la EDO 
$$
q(t)=Q\cos(\omega t)=Q\cos\left( \frac{t}{\sqrt{ LC }} \right)
$$
Gracias a que me mostraste las condiciones iniciales, aunque claro son las que vimos antes, pero antes de ellas había llegado a 
$$
q(t)=q(0)\cos(\omega t)+\frac{\dot{q}(0)}{\omega}\sin(\omega t)
$$
Que siendo el primer termino el que va siguiendo los ciclos de la carga de ${}+Q \to 0 \to -Q{}$ , pero el segundo no veo bien su uso. 
Mientras que la corriente al derivar ya la solución con las condiciones iniciales
$$
\frac{d}{dt} q(t)=-Q \sin(\omega t)\omega = \frac{-Q\sin\left( \frac{t}{\sqrt{ LC }} \right)}{\sqrt{ LC }}
$$
Si no me estoy equivocando en alguna derivada o signo, con ${}i(t)=\frac{dq(t)}{dt}{}$
Me equivoque en los signos, tenemos la convención de que una descarga de las cargas es una corriente positiva 
$$
i(t)=-\frac{d}{dt} q(t) \to i(t)= Q\sin(\omega t)\omega 
$$
Cosa que concuerda con la interpretación física de que al descargar el capacitor va aumentado la corriente, disminuye la carga implica derivada negativa, lo que indica un aumento de la corriente

La energía total queda 
$$
U_{total}(t)=\frac{1}{2} \frac{Q^{2}}{C}
$$
siendo el principal truco aprovechar que están elevando a 2 el ${}q(t)^{2},i(t)^{2}{}$, ya que al hacerlo y simplificando con $\omega_0=\frac{1}{\sqrt{ LC }}$ nos va a quedar la expresión 
$$
U_{total}(t)=\frac{1}{2} \frac{Q^{2}}{C}(\cos(\omega t)^{2}+\sin(\omega t)^{2})
$$
que podemos simplificar.  Eliminando t y quedando que la energía total va a ser constante en el tiempo

Las tensiones en un circuito RCL
$$
v_{L}=L\frac{di}{dt} \quad v_{R}=Ri \quad v_{C}=\frac{q}{C}
$$
Lo cual siguiendo las leyes de Kirchoff deben de sumar 0, dándonos la EDO 
$$
L\frac{di}{dt}+Ri+\frac{q}{C}=0 \implies L\frac{d^{2}q}{dt^{2}}+R\frac{dq}{dt}+\frac{q}{C}=0
$$
Aplicando los valores dados: ${}R=2 \Omega, L=1H,C=\frac{1}{4}F{}$
$$
\ddot{q}+\frac{2\Omega}{1H}\dot{q}+q \frac{4}{HF}=0
$$
No entiendo como hacer una derivada numérica, creo que si simplemente tomo t=0 y aplico me deberia de dar todo cero, si tomo ${}\dot{q}=0 \to \ddot{q}=0 \to \frac{q}{LC}=0{}$  lo que creo que no es la idea.  Para la segunda al calcular 
$$
b=\frac{R}{2L} \implies b=1 \frac{\Omega}{H} \leq  \omega_{0}=\frac{1}{\sqrt{ LC }}\to \omega_{0}=2  \frac{1}{\sqrt{ HF }}
$$
Siendo en este caso su comportamiento del circuito subamortiguado.
Para la tercera, al incluir una resistencia al circuito el cambio de energía total pasa a ser negativo lo que indica que la energía va disminuyendo en el tiempo, mostrándose en una perdida térmica que sucede en la resistencia del circuito, esto sucede, ya que al agregar la resistencia agregamos el término de potencia disipada que ~~siempre~~ mientras haya corriente  va a ser negativo en el cambio de energía total al siempre ser un término positivo 

Al resolver la edo hasta llegar a la ecuacion que me diste 
$$
Q(s)=Q  \frac{s+2}{(s+1)^{2}+3} = Q\left[ \frac{s+1}{(s+1)^{2}+3}+ \frac{1}{\sqrt{ 3 }} \frac{\sqrt{ 3 }}{(s+1)^{2}+3} \right]
$$
Desde ahí aplicamos su inversa y gracias a que me diste la pista (no me acordaba que hacer con el s+1) 
$$
q(t)=Q\cos(\sqrt{ 3 }t)e^{ -t }+\frac{Q}{\sqrt{ 3 }}\sin(\sqrt{ 3 }t)e^{ -t }
$$
No me acuerdo bien de las traslaciones para laplace, pero en este ejercicio creo que llegamos a eso