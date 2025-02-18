# Program that is going to calculate the number of digits in the binary expansion/representation of integer n (positive integer)
import math
def bin_rep(n):
    '''Function that calculate the number of digits in 
        the binary expression/representation of a positive integer n.
        
    Input:
        n = positive integer
        
    Output:
        integer value representing the total number of digits
        in the binary representation/expansion of n'''
    
    if n == 0:
        return 0
    return 1 + bin_rep(n // 2)
    
print(bin_rep(750))