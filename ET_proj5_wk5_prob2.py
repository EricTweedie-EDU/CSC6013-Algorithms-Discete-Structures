# program that takes an array and bubble sorts the array into ascending order with the possibility of an early exit if no swaps happen

def bubbleSort(x):
    '''function that does the bubble sort method on an array.
    Function will also end early if there are no swaps that occur.
    
    Input: 
        array of integers
    
    Output:
        sorted array of integers in ascending order'''
    total_swaps = 0
    total_compares = 0
    for i in range(len(x)-1):
        swaps = 0
        compare = 0
        for j in range(len(x)-i-1):
            if (x[j] > x[j+1]):
                x[j], x[j+1] = x[j+1], x[j]
                swaps += 1
                compare += 1
                print(swaps)
                print(compare)
                print(x)
                total_swaps += swaps
                total_compares += compare
    
    print(f"The total # of comparisons is: {total_compares}\n")
    print(f"The total # of swaps is: {total_swaps}\n")
    print(f"The sorted array: {x}")


A4 = [44,63,77,17,20,99,84,6,39,52]
A5 = [52,84,6,39,20,77,17,99,44,63]
A6 = [6,17,20,39,44,52,63,77,84,99]

bubbleSort(A6)