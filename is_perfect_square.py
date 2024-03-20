#The following is a code that checks if the input is a perfet square or not.
#written by Viren Hemrajani, 500089749.

def is_perfect_square(n):
    """Check if a number is a perfect square."""
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n

