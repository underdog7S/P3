#T1


n1= int(input("Enter the number: "))

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

result= factorial(n1)
print("Factorial of",n1, "is", result)


#T2

import math


number = float(input("Enter a number: "))


square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)

# Displaying the results
print("Square root:", square_root)
print("Natural logarithm:", natural_log)
print("Sine:",  sine_value)

