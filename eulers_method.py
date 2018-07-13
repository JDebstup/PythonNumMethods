'''
First-Order Euler's Method Automation Program
Version 0.1
Written by Jay Piamjariyakul (github.com/JDebstup)
Compatible with Python 3 or greater

1) Initial setup
'''
#from __future__ import division
import numpy as np #imports numpy, and lets us use it as 'np'
from scipy.integrate import odeint
from matplotlib import pyplot as plot
#import tkinter as tk

print("First-Order Euler's Method Automation Program v 0.1")
print("By Jay Piamjariyakul (github.com/JDebstup)")
print("Compatible with Python 3 or greater")
print("")
print("Note: Enter all inputs as numpy-compatible expressions")
print("")
equation_input = input("Enter ODE (of form x = f(t)), where differential is solely on the other side: ")
print("")

#defines RHS of differential equation
#to use, input RHS of equation to use in Euler's Method here
def diff(x, t):
    #print(equation_input)
    equation = eval(equation_input)
    return (equation)

'''
2) Sets user parameters of finding approximation via numerical method
'''
in_initial = eval(input("Enter initial input for ODE: "))
out_initial = eval(input("Enter initial output for ODE: "))
step_single = eval(input("Enter step size: "))
step_max = eval(input("Enter max value to step to: " ))

'''
3) Finds true solution to ODE
'''
var_in_true = np.linspace(in_initial, step_max, ( (step_max - in_initial) / 0.1 ))
# NOT "arrange"!
var_out_true = odeint(diff, out_initial, var_in_true)

'''
4) Sets further internal variables
'''
step_total = int(round((( step_max - in_initial ) / step_single), 2))

#Defines discrete time t, assuming no remainders exist when dividing step_max by step_single
step_current = in_initial

#Defines array to store values on the independent axis
var_in_num = []
#sets loop for iterations to range
# Loops over "+1" to compensate for the final value as well
for counter in range(step_total + 1):
    var_in_num.append(step_current)
    step_current += step_single
    
#Defines array to store numerical solution
var_out_num = []
#sets initial condition as initial result
var_out_num.append(out_initial)

'''
5) Computes numerical solutions
'''
#loops over given range, applying Euler's method, until the final values are achieved
for counter in range(step_total):
        answer = var_out_num[counter] + ( step_single * diff(var_out_num[counter], var_in_num[counter]) )
        var_out_num.append(answer)

'''
6) Plots solutions on graph
'''
plot.plot(var_in_true, var_out_true, color="red", linestyle=":", label="True")
plot.plot(var_in_num, var_out_num, marker="x", color="green", linestyle="--", label="Numerical")

plot.xlabel("Input")
plot.ylabel("Output")
plot.title("Computing 1st-order ODE w/ Euler's Method")
plot.suptitle("ODE: " + equation_input)
plot.legend(("Numerical", "True"))

print()
print("Plot shown")

plot.show()

