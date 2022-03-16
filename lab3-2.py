# Author: CCG 3/16/2022

def factorial(num):
    if num != 0:
        total = 1 
        counter = 1
        while counter <= num:
            total *= counter
            counter += 1
        return total
    else:
        print("This function cannot handle zero as an input")

print(factorial(0))
print(factorial(5))