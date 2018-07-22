'''
1) Initial setup
'''
#from __future__ import division
import numpy as np #imports numpy, and lets us use it as 'np'
from scipy.integrate import odeint
from matplotlib import pyplot as plot
#import tkinter as tk

print("First-Order Euler's Method Automation Program v 0.4")
print("By Jay Piamjariyakul (github.com/JDebstup)")
print("Compatible with Python 3 or greater")
print("")
print("Note: Enter all inputs as numpy-compatible expressions")
print("E.g. np.pi, np.e**x, np.sin(t), etc (refer to numpy documentation for details)")
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
var_out_num_forw = []
var_out_num_back = []
#sets initial condition as initial result
var_out_num_forw.append(out_initial)
var_out_num_back.append(out_initial)

'''
5) Computes numerical solutions for forward Euler
'''
#loops over given range, applying Euler's method, until the final values are achieved
for counter in range(step_total):
    answer = var_out_num_forw[counter] + ( step_single * diff(var_out_num_forw[counter], var_in_num[counter]) )
    var_out_num_forw.append(answer)
        
'''
6) Computes numerical solutions for backward Euler
'''

# Creates a hidden true solution, but with the number of elements to use
# Copies directly from original numerical input array, but we just add one more to allow back method to work!
var_in_hidden = var_in_num.copy()
var_in_hidden.append(var_in_num[len(var_in_num) - 1] + step_single)
# Now, we can just integrate & substitute for each of the values!
var_out_hidden = odeint(diff, out_initial, var_in_hidden)
# We don't actually need the first value at [0] because for n = 0, we'd want the diff at n+1!

for counter in range(step_total):
    # Integrates at the next point first, then go back to the previous point
    # Uses hidden input & output arrays to help find the next points!
    #print("Diff: ", var_out_hidden[counter + 1], " & ", var_in_hidden[counter + 1], " => ", diff(var_out_hidden[counter + 1], var_in_hidden[counter + 1]))
    answer = var_out_num_back[counter] + ( step_single * diff(var_out_hidden[counter + 1], var_in_hidden[counter + 1]))
    var_out_num_back.append(answer)

'''
7) Plots solutions on graph
'''
plot.suptitle("ODE: " + equation_input)

var_true, = plot.plot(var_in_true, var_out_true, color="red", linestyle=":", label="True")

plot.subplot(2, 1, 1)
plot.title("Computing 1st-order ODE w/ Euler's Method")
var_true, = plot.plot(var_in_true, var_out_true, color="red", linestyle=":", label="True")
var_forw, = plot.plot(var_in_num, var_out_num_forw, color="green", linestyle="-", label="Forward")
plot.ylabel("Forward")
plot.legend(handles=[var_true, var_forw])
plot.minorticks_on()
plot.grid(b=True, which='major', color='0.5', linestyle='-')
plot.grid(b=True, which='minor', color='0.75', linestyle='--')

plot.subplot(2, 1, 2)
#var_back_true, = plot.plot(var_in_true, var_out_true, color="red", linestyle=":", label="True")
var_true, = plot.plot(var_in_true, var_out_true, color="red", linestyle=":", label="True")
var_back, = plot.plot(var_in_num, var_out_num_back, color="blue", linestyle="-", label="Backward")
plot.ylabel("Backwards")
plot.legend(handles=[var_true, var_back])
plot.minorticks_on()
plot.grid(b=True, which='major', color='0.5', linestyle='-')
plot.grid(b=True, which='minor', color='0.75', linestyle='--')

plot.xlabel("Input")
print()
print("Plot shown")

plot.show()
