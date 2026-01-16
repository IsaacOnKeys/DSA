## WRITE INSERTION_SORT FUNCTION HERE ##
def insertion_sort(myArray):

    for i in range(1, len(myArray)):
        temp = myArray[i]
        j = i-1
        while temp > myArray[j] and j > 0:
            





print(insertion_sort([4,2,6,5,1,3]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """

