'''
This function creates a star pattern like this....
    *
   ***
  *****
 *******
*********
Written by- Ayush Paliwal 
Course    - BCA (CSF)
SapId     - 500094587
Roll No.  - R252221071 

'''






def star_triangle(rows):
    for i in range(rows):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))

# Example usage:
star_triangle(5)
