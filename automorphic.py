def automorphic_500089748(n):

    ''' 

    This function checks whether a number is an Automorphic number or not. 

    An Automorphic number is a number whose square ends with the same digits as the number itself.
    
    Written by : Gunpreet Kaur | 500089748  

    '''

    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n <= 0:
        raise ValueError("Input must be a positive integer")

    square = n ** 2
    # Compare the last digits of the number and its square
    return str(square)[-len(str(n)):] == str(n)


if __name__== '__main__':
    print(automorphic_500089748(5))
