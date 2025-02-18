# program that calculates the sum of squares of the positive integer n

def square_sum(n):
    '''Function that calucates the sum of squares from the positive integer n.
    Calculates the sum of squares from 1**2 to n-1**2 + n**2.
    
    Input:
        n = postive integer value
    Output:
        integer value = sum of squares from 1 to n-1'''
    
    if n == 1:
        return 1
    else:
        return n**2 + square_sum(n-1)

    
print(square_sum(20))