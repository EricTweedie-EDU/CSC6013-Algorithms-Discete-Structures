# progrmam the calculates the arithmetic of an array that represents a polynomial function
# program has 2 functions, 1 that calculates the p'th power of a real number
# the other function evaluates the function and makes a call to the power function for the given coefficients

# polynomial function = f(x) = 12.3 + 40.7x - 9.1x**2 + 7.7x**3 + 6.4x**4 + 8.9x**6
def power(x, p):
    '''Function that takes a given value of X and calculates the power 
    from the exponent power P from a given array of integers.
    P is based off the indeces of the array for each given value in the array.
    X is the value that is being plugged into the polynomial function from f(x).
    
    Parameters: value X and value P are inputted into the function and the power of 
    x**p is calculated, but the calculation is done without using the ** operator.

    Input: 
        x = intger/floating point number
        p = integer value of the index from the given array
    
    Output:
        integer/floating point number value that is from the calculation 
        of x to the power of p,  x**p.'''
    
    numbers = [] # empty list to store values
    res = 1
    for i in range(len(p)):
        if p[i] == 0:
            continue
        else:
            res *= x
            numbers.append(res)
    return numbers
            

A = [12.3, 40.7, -9.1, 7.7, 6.4, 0, 8.9]
x = 5.4
power(x, A)


# funtion that evaluates the polynomial function that determines the value of f(x) in the polynomial function
def evaluate(A, x):
    '''Function that evaluates the given f(x) from the polynomial function
    that corresponds to the array used. Function makes a call to the power()
    function for each given part of the polynomial function.
    
    Input:
        A = the array of integers/floating point numbers from the polynomial function
        x = the f(x) value that is being plugged into the function
        
    Output:
        integers/floating point numbers that are the result of the caclulations of the 
        polynomial function f(x)'''
    
    z = [] # empty list to store array values
    c = [] # empty list to store the coefficent values from power()
    f = [] # empty list to store the values from total
    n = 0
    for i in range(1, len(A)):
        num = A[i]
        z.append(num)
    for j in power(x, A):
        y = j
        c.append(y)
    for _ in range(len(z)) and range(len(c)):
        total = z[_] * c[_]
        f.append(total)
    for _ in range(len(f)):
        n += f[_]
    
    answer = (A[0] + n)
    print(f"The final answer is: {round(answer, 4)}")
    
evaluate(A, x)       