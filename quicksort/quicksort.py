def swap(A, i, j):

    temp = A[i]
    A[i] = A[j]
    A[j] = temp

#Lomuto partition scheme
def partition(a, start, end):

    #set pivot to rightmost element of a
    pivot = a[end]

    pIndex = start

    #each time we find an element less than or equal to pivot
    #pIndex is incremented and that element placed before pivot
    for i in range(start, end):
        if a[i] <= pivot:
            swap(a, i, pIndex)
            pIndex += 1
    
    #swap pIndex with pivot
    swap(a, end, pIndex)

    return pIndex

def quicksort(a, start, end):

    if start >= end:
        return

    pivot = partition(a, start, end)

    #recur on a sublist containing elements less than pivot
    quicksort(a, start, pivot-1)

    #recur on a sublist containing elements more than pivot 
    quicksort(a, pivot+1, end)

if __name__ == "__main__":

    a = [9, -3, 5, 2, 6, 8, -6, 1, 3]
 
    quicksort(a, 0, len(a) - 1)
 
    # print the sorted list
    print(a)