from sympy import simplify
from sympy.abc import x,y
vers1 = (x+y)**2
vers2 = x**2 + 2*x*y + y**2
a=simplify(vers1-vers2) == 0
b=simplify(vers1+vers2) == 0
print(a)
print(b)
