# Program that given an integer of n>=2 and two matrices A and B of real numbers, find the product AB of the matrices

# function that takes a positive integer and 2 NxN matrices of numbers and produces the product of the NxN matrices

def matrix_product(x, y, z):
    '''Function that takes a positive integer and 2 NxN matrices of numbers
    and then will calculate the product of the NxN matrices. The result of the function
    is the NxN product matrix.
    
    Input: 
        x = positive integer
        y = NxN matrix with real numbers
        z = the 2nd NxN matrix with real numbers
        
    Output:
        NxN matrix which is the product of the 2 input matrices.'''
    
    # starting with 0 matrix
    result = [[0 for j in range(x)] for i in range(x)]

    # iterating through the rows of y
    for i in range(len(y)):
        # iterating through the columns of z
        for j in range(len(z[0])):
            # iterating through the rows of z
            for k in range(len(z)):
                result[i][j] += round(y[i][k] * z[k][j], 2)
    return result




x = 2
a = [[2, 7], [3, 5]]
b = [[8, -4], [6, 6]]
print(matrix_product(x,a,b))