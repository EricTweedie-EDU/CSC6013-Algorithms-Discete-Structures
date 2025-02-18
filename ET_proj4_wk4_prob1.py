# Program finding the number of entries in an array if integers that are divisible by a given integer.
# Should return the count as an integer using return statement

# function that takes array and a given integer to find how many entries are divisible by that given number

def divisible_count(x, y):
    '''Function that takes an input of an array and a given integer 
        to calculate how many of the entries are divisible by that 
        given integer.
        
        Inputs:
            x = array of integers
            y = integer value used to check division
            
        Output:
            Integer: the count of how many entries are divisible by input y'''
    count = 0
    for i in x:
        if i % y == 0:
            count += 1
        else:
            pass
    return count
    

a = [20, 21, 25, 28, 33, 34, 35, 36, 41, 42]
c = 7

b = [18, 54, 76, 81, 36, 48, 99]
d = 9

print(divisible_count(a,c))