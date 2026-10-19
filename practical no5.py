#---Built-in Module---
import math
num=16
print("Square root of",num,"is",math.sqrt(num))
print("Factorial of",num,"is",math.factorial(num))
print("Power of",num,"is",math.pow(num,2))
print("Log:",math.log(10))

#---Functional Programming Module---
from functools import reduce
numbers=[1,2,3,4,5,]
result=reduce(lambda x,y:x+y,numbers)
print("Sum of numbers:",result)

#---User-defined Module Concept---
def add (a,b):
    return a+b

def multiply(a,b):
    return a*b

import my_module

print("Addition of 5 and 3 is:",my_module.add(5,3))
print("Multiplication :",my_module.multiply(4,2))