# Program that performs Quick Select algorithm and for an array of n elements finds the k-th smallest element of the array
import random

def partition(list, l, r):
    '''Function that is apart of the quick select algorithm to sort the array
    based on the pivot value of the array, last element is the pivot. Sorts the array into
    values less than the pivot, pivot, and values greater than the pivot.
    Input:
        list = array of integers
        l = integer, left (lesser values than pivot) side of partition
        r = integer, right (greater values than pivot) side of partition
    Output:
        partitioned array based on pivot value'''
    x = list[r]
    i = l
    for j in range(l, r):
        if list[j] <= x:
            list[i], list[j] = list[j], list[i]
            i += 1

    list[i], list[r] = list[r], list[i]
    return i

def QuickSelect(list, l, r, k):
    '''Function that is performing the quick select algorithm to find
    the k-th smallest element in an array of n elements.
    Input:
        list = array of integers
        l = left most end of the array, integer value
        r = right most end of the array, integer value
        k = integer value for the k-th smallest value of array
    Output:
        Int = k-th smallest integer value within the array'''
    # if k is smaller than number of elements in array
    if (k > 0 and k <= r - l + 1):
        index = partition(list, l, r) # partition array around last element and get position of pivot
    # if position is same as k
    if (index - l == k -1):
        return list[index]
    # if position is more, call for left subarray
    if (index - l > k - 1):
        return QuickSelect(list, l, index - 1, k)
    # call/recur for right subarray
    return QuickSelect(list, index + 1, r, k - index + l - 1)

# Driver code
# array of random integers, total of 1000 elements
x = []
n = 1000
for i in range(n):
    x.append(random.randint(0,2000))

y = len(x)
k = int(input("Please enter a positive number from 0 - 1000 to find in the array x: "))
print(f"The k-th smallest element at index {k} is: {QuickSelect(x, 0, n-1, k)}")