from math import sqrt

def armstrong_500089748(n):
    ''' 
    This function checks whether a number is an Armstrong number or not. 
    An Armstrong number is a number that is equal to the sum of its own digits 
    each raised to the power of the number of digits.
    
    Author: Gunpreet Kaur | 500089748  
    '''

    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n <= 0:
        raise ValueError("Input must be a positive integer")

    # Convert the number to a string to count digits
    num_str = str(n)
    # Calculate the number of digits
    num_digits = len(num_str)
    # Initialize sum of powered digits
    armstrong_sum = 0
    # Iterate through each digit and raise it to the power of the number of digits
    for digit in num_str:
        armstrong_sum += int(digit) ** num_digits
    
    # Check if the sum equals the original number
    if armstrong_sum == n:
        return "Armstrong Number"
    else:
        return "Not an Armstrong Number"
    

if __name__== '__main__':
    print(armstrong_500089748(153))
