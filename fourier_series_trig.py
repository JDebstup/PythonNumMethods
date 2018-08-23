#import sympy as sp
#from sympy import oo, pi
from pprint import pprint
import scipy as sc
from scipy import integrate

import numpy as np
#import math
from matplotlib import pyplot as plot

print("Fourier Series Visualizer v 0.3")
print("By Jay Piamjariyakul (github.com/JDebstup)")
print("Compatible with Python 3 or greater")
print("")
print("Note: Enter all inputs as sympy-compatible expressions")
print("E.g. pi, e**x, sin(x), etc (refer to sympy documentation for details)")
print("")

'''
while True:
    equation_input = input("Enter equation (in form of y=f(x)) for which is to be transformed: ")
    print("")
    if ("x" not in equation_input):
        print("ERROR: Enter valid equation")
        print("NOTE: If you wish to enter coefficients, enter them as k * (x**0)")
    else:
        break
'''
equation_input = input("Enter equation (in form of y=f(x)) for which is to be transformed: ")
def equation(x):
    return eval(equation_input)

def term_a(x):
    return eval("(" + equation_input + ") * sc.cos(n*x)")
def term_b(x):
    return eval("(" + equation_input + ") * sc.sin(n*x)")

var_in = np.linspace((-2 * np.pi), (2 * np.pi), ( 4 * np.pi / 0.1 ))

n_max = int(input("Enter number of times for term of n for series to transform to: "))

print()
print("Calculating...")
#n = sp.Symbol("n")

#a_0 = (1/(2 * np.pi)) * integrate.quad(equation, -np.pi, np.pi)[0]
#x = sp.Symbol("x")
var_out_eq = []

for index in var_in:
    if (index < -np.pi):
        var_out_eq.append(equation(index + (2 * np.pi)))
    elif (index > np.pi):
        var_out_eq.append(equation(index - (2 * np.pi)))
    else:
        var_out_eq.append(equation(index))

#print(var_out_eq)
print()

var_out_fourier = []

a_0 = (1/(2 * sc.pi)) * integrate.quad(equation, -sc.pi, sc.pi)[0]
for index in var_in: # loops over each value of x
    sum_current = a_0; # sets DC value offset
    for n in range(1, (n_max + 1)): # for each value of n, nEZ
        print("Calculating for n = " + str(n) + " with x = " + str(index))
        a_n_current = (1/sc.pi) * integrate.quad(term_a, -sc.pi, sc.pi)[0]
        term_cos = a_n_current * sc.cos(n * index) # multiplies each a_n by term of cos at current x and n
        b_n_current = (1/sc.pi) * integrate.quad(term_b, -sc.pi, sc.pi)[0]
        term_sin = b_n_current * sc.sin(n * index) # multiplies each b_n by term of sin at current x and n
        sum_current += (term_cos + term_sin) # adds S[(a_n * cos(nx)) + (b_n * sin(nx)] from 1 to n_max
    var_out_fourier.append(sum_current) # sets such current sum as fourier-equivalent value at such point


plot.suptitle("f(x): " + equation_input)

plot.title("Fourier Series Visualization")
var_eq, = plot.plot(var_in, var_out_eq, color="red", linestyle="-.", label="True")
var_fourier, = plot.plot(var_in, var_out_fourier, color="green", linestyle=":", label="Fourier")
plot.ylabel("f(x)")
plot.legend(handles=[var_eq, var_fourier])
plot.minorticks_on()
plot.grid(b=True, which='major', color='0.5', linestyle='-')
plot.grid(b=True, which='minor', color='0.75', linestyle='--')

plot.xlabel("x")
print()
print("Plot shown")

plot.show()
