## WRITE BUBBLE_SORT FUNCTION HERE ##
def bubble_sort(my_list):
    # list_length = len(my_list)
    
    for index in my_list:
        first = my_list[index]
        second = my_list[index + 1]
        if second is not None and first > second:
            first, second = second, first

##################################### 



print(bubble_sort([4,2,6,5,1,3]))

 

"""
    EXPECTED OUTPUT: 
    ----------------
    [1, 2, 3, 4, 5, 6]
 """