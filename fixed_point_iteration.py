import numpy as np
from matplotlib import pyplot as plot

print("Fixed-Point Iteration Automation Program v 0.1")
print("By Jay Piamjariyakul (github.com/JDebstup)")
print("Compatible with Python 3 or greater")
print("")
print("Note: Enter all inputs as numpy-compatible expressions")
print("E.g. np.pi, np.e**x, np.sin(t), etc (refer to numpy documentation for details)")
print("")
equation_input = input("Enter equation (of form x = g(x)), where g(x) is solely on the other side: ")
print("")

def fixed_point(x):
    #print(equation_input)
    equation = eval(equation_input)
    return (equation)

in_initial = eval(input("Enter initial guess for equation: "))
loop_total = eval(input("Enter number of times to iterate for: "))

# Output value, used as next input
var_out_num = []
var_out_num.append(in_initial)
for counter in range(loop_total):
    # Uses previously obtained value to 
    var_out_num.append(fixed_point(var_out_num[counter]))
    
# Creates input array containing the counters' values 
var_in_num = np.linspace(0, loop_total, len(var_out_num))

var_in_true_eq = np.linspace(min(var_out_num), max(var_out_num), ( (max(var_out_num) - min(var_out_num)) / 0.1 ))
var_out_true_eq = fixed_point(var_in_true_eq)

var_in_true_x = np.linspace(min(var_out_num), max(var_out_num), ( (max(var_out_num) - min(var_out_num)) / 0.1 ))
var_out_true_x = var_in_true_x.copy()
#print(var_in_true_x)
#print(var_out_true_x)

plot.suptitle("Fixed-point: " + equation_input)

plot.subplot(1, 2, 1)
plot.title("Finding root of equation with fixed-point iteration")
plot.plot(var_in_num, var_out_num, marker="x", color="blue", linestyle="-", label="True")
plot.legend(("X"))
plot.xlabel("Counter")
plot.ylabel("Root")

plot.subplot(1, 2, 2)
plot.title("Visualization of FPI")
plot.plot(var_in_true_eq, var_out_true_eq, color="green", linestyle=":", label="True")
plot.plot(var_in_true_x, var_out_true_x, color="red", linestyle=":", label="True")
plot.legend((("y = " + equation_input), ("y = x")))
plot.xlabel("x")
plot.ylabel("y")


print()
print("Plot shown")

plot.show()
