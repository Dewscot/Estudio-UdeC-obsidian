$$
f(x) \approx f(x_{0})+ f'(x_{0}) \frac{(x-a)}{1} + f''(x_{0}) \frac{(x-a){^2}}{2} +\dots. +f{^n}(x_{0}) \frac{(x-a){^n}}{n!}
$$
SI eso es la serie de taylor para x, si tomamos x+h pienso que simplemente deberiamos de remplazar el valor de x de la ecuacion por x+h lo que nos daría:
$$
f(x+h)=f(x_{0})+f'(x_{0}) \frac{x+h-x_{0}}{1}+f''(x_{0}) \frac{(x+h-x_{0})^{2}}{2}+ \dots 
$$

siendo el x+h la funcion que queremos aproximar mientras que $x_0$ es el centro de la expansión.
Pero si queremos que el centro sea x tenemos $x=x_0$ lo que nos deja 
$$
f(x+h)=f(x)+f'(x)h+f''(x) \frac{h^{2}}{2} +\dots
$$
Si intentamos despejar $f'(x)$ tenemos 
$$
\frac{f(x+h)-f(x)}{h}=f'(x)+f''(x) \frac{h}{2}+\dots
$$ 
Que es la derivada adelantada es igual a ${}f'(x){}$ más los otros terminos, pero como vimos que cuando más pequeño es h menos afecta al resultado o menos importa así que su ${}O(h) {}$ es de primera magnitud 