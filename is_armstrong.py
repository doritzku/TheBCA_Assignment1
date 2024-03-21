'''
This function finds out whether a given number is an Armstrong number or not.
Written by Sanya Mehta 
Sap id: 500092051

'''

def is_armstrong(num):
    
    # Convert number to string to iterate over its digits
    num_str = str(num)
    # Calculate the power (order) of the number
    order = len(num_str)
    
    # Initialize sum
    sum= 0
    
    # Iterate over each digit
    for digit in num_str:
        # Convert digit back to integer and raise to the power of order
        sum += int(digit) ** order
    
    # Check if the sum equals the original number
    return num == sum

# Take input 
num = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")


