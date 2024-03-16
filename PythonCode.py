from math import sqrt

''' Hello '''
''' Please Contribute'''

# Example code
    
def prime_300(n):
    ''' This code check whether a number is prime number or not 
        Author: Senior Developer at ABC  '''
    
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    if n == 1:
        return "Not a Prime Number!!"
    elif n > 1:
        for j in range(2, int(n**0.5) + 1):
            if n % j == 0:
                return "Not a Prime Number"
        else:
            return "Prime Number"

        
           



if __name__== '__main__':
    print(prime_300(8))
