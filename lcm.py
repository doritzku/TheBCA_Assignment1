#Code written by Namra Tyagi, 500091016
def gcd(a, b):
    """Calculate the greatest common divisor (GCD) of two numbers."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Calculate the least common multiple (LCM) of two numbers."""
    return (a * b) // gcd(a, b)

