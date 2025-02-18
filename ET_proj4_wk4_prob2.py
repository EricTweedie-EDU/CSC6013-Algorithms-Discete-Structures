# Program that given  an array of real numbers, without sorting the array, find the smallest gap between all pairs of elements

# function that takes an array and calculates the smallest gap between pairs of elements

def smallest_gap(x):
    '''function that takes an array as input and calculates the smallest 
    gap between pairs of elements. Returns integer value that indicates the smallest gap.
    
    Input:
        x = Array of real numbers
        
    Output:
        Integer: non-negative number indicating the smallest gap'''
    
    # setting gap to infinite
    gap = 10**20

    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if abs(x[i] - x[j]) < gap:
                gap = abs(x[i] - x[j])
    return gap

a = [50, 120, 250, 100, 20, 300, 200]

b = [12.4, 45.9, 8.1, 79.8, -13.64, 5.09]

print(smallest_gap(b))