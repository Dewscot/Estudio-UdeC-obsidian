Generalizacion de la rama principal
$$
Log^{\alpha}(z)=\ln|z|+i\theta \quad , \alpha <\theta<\alpha+2\pi
$$
Las preguntas que me diste. 
1. Al tomar ${}Log{^0} {}$ estamos excluyendo la semirrecta real positiva, del (0,${}+\infty{}$), pero la función esta definida como${}f(z)=Log{^0}(z-1){}$ por lo que el termino ${}z-1{}$ cambia el dominio del logaritmo lo que mueve esa semirrecta 1 hacia la derecha quedando que no incluye ${}(1,+\infty){}$ 
2. Si esta definida ${}f(0){}$ para el domino que tenemos mientras que ${}f(2){}$ no esta definida 
3. Entiendo que es diferente el dominio ya que estamos excluyendo distintas semirrectas para cada rama, para que siga siendo biyectiva el Log y se pueda ocupar con el exponencial. Pero la exacta razón, no lo se. Son diferentes por los ángulos que permiten y por ello mismo los complejos que aceptan 
Si tomamos la expresión ${}z(t)=1+2e^{it},0\leq t\leq 2\pi{}$ su derivada será ${}z'(t)=2ie^{it}$ por lo que la integral quedara: 
$$
	\int_{0}^{2\pi} \frac{1}{1+2e^{it}-1} 2ie^{it} \, dt = \int_{0}^{2\pi} i \, dt 
$$

Fue un error al anotarlo el que pusiera ${}e^{2it}{}$ en vez de la que me diste, pero tal y como dices es interesante 
Haciendo los cálculos me quedaron 
$$
\frac{1}{z^{2}+1} =\frac{A}{z-1}+\frac{B}{z+1} = -\frac{i}{z-1}+\frac{i}{z+1}
$$
Si derivamos:
$$
f(z)=\frac{e^{z}}{z} \to f'(z)=\frac{e^{z}z-e^{z}}{z^{2}} \to f'(1)=\frac{e-e}{1}=0
$$

Separando en fracciones parciales 
$$
\frac{1}{z(z-1)^{2}}=\frac{1}{z}-\frac{1}{z-1}+\frac{1}{(z-1)^{2}}
$$
Que tenemos que multiplicar por ${} {}$ 
$$
e^{z} \to \frac{e^{z}}{z(z-1)^{2}}=\frac{e^{z}}{z}-\frac{e^{z}}{z-1}+\frac{e^{z}}{(z-1)^{2}}
$$
Que nos daría la integral quedando
$$
I=\oint_{C}\frac{e^{z}}{z}dz-\oint_{C}\frac{e^{z}}{z-1}dz+\oint_{C}\frac{e^{z}}{(z-1)^{2}}dz
$$

sabemos que ${}f(z)=f'(z)=f''(z)=e^{z}{}$ lo que implica que ${}f(0)=1,f(1)=f'(1)=e{}$
quedando 
$$
I=2\pi i -e 2\pi i+e 2\pi i =2\pi i
$$
