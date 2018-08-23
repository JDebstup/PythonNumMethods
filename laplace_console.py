import sympy
from sympy import oo
import pprint

print("Laplace Transform v 0.1")
print("By Jay Piamjariyakul (github.com/JDebstup)")
print("Compatible with Python 3 or greater")
print("")
print("Note: Enter all inputs as sympy-compatible expressions")
print("E.g. pi, e**x, sin(t), etc (refer to sympy documentation for details)")
print("")

equation_input = input("Enter equation (in form of x=f(t)) for which is to be transformed: ")
print("")

while True:
    if ("t" not in equation_input):
        print("ERROR: Enter valid equation")
    else:
        break
    
'''
def equation(t):
    equation = eval(equation_input)
    return (equation)
'''

t = sympy.Symbol("t")
s = sympy.Symbol("s")

print("Laplace-transform of " + equation_input + ": ")
result = sympy.integrate((sympy.exp(-s * t) * eval(equation_input)), (t, 0, oo))
    
pprint.pprint(result)