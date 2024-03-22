'''
This function finds the factorial of a number.
Written by Dhruv Aggarwal
Sap id: 500094811

'''


def factorial(n):
    # Checking if the number is negative   
    if n < 0:    
        raise ValueError("Factorial does not exist for negative numbers")   

    # Initializing the factorial variable to 1 
    result = 1

    # Calculating factorial if the number is positive
    for i in range(1, n + 1):    
        result *= i    

    return result