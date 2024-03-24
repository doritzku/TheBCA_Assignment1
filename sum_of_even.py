#written by arpita bhardwaj, 500089338

def sum_of_even(n):
    """Find the sum of all even numbers up to a given integer."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    return sum(i for i in range(2, n + 1, 2))

