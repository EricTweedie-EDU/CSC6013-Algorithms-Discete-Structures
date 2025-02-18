# program that uses selection sort algorithm to sort an array in ascending order
# sorting by the largest elements to sort the array

def selectionSort(x):
    '''Function that is taking the elements of an array
       and sorting them by the LARGEST number element in the array.
       End result is in ascending order.
       
       Input:
            Array of integers
        
        Output:
            Sorted array of integers in ascending order'''
    
    for i in range(len(x)-1):
        swaps = 0  # checking to see how many times each element is swapped
        compare = 0 # checking to see how many time each element is compared
        minIndex = i
        for j in range(i+1, len(x)):
            if (x[j] < x[minIndex]):
                minIndex = j
            x[i], x[minIndex] = x[minIndex], x[i]
            swaps += 1
            compare += 1
            print(swaps)
            print(compare)
            print(x)
    
    return x

A1 = [63,44,17,77,20,6,99,84,52,39]
A2 = [84,52,39,6,20,17,77,99,63,44]
A3 = [99,84,77,63,52,44,39,20,17,6]


selectionSort(A3)
print(selectionSort(A3))