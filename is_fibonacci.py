'''
This function finds out whether a given number is a fibonacci number or not.
Written by Ankur Kumar 
Sap id: 500090333
Course: BCA (CSF)
'''

import math

def is_perfect_square(n):
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def is_fibonacci_number(num):
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

if __name__ == "__main__":
    try:
        number = int(input("Enter a number to check if it's a Fibonacci number: "))
        if is_fibonacci_number(number):
            print(number, "is a Fibonacci number.")
        else:
            print(number, "is not a Fibonacci number.")
    except ValueError:
        print("Please enter a valid integer.")