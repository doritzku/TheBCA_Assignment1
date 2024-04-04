def subtract_values(a, b):
    try:
        result = a - b
        return result
    except TypeError:
        return "Error: Both inputs must be numeric values."