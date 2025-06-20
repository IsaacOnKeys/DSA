"""
Insertion Sort:
 1. Compare first 2 elements
 2. If the secone is greater than the first, we shift the first to the right, and insert the first before it.
 3. We continue throught the list, and with each smaller number found, we send it towrd the front, shifting the larger numbers past it.
 ---------------------------------

 Complexity:
 Worst and average cases: n^2
 Best Case: Omega(n)
"""

# Insertion sort implementation


def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        number_to_order = my_list[i]
        j = i - 1
        while j >= 0 and number_to_order < my_list[j]:
            my_list[j+1] = my_list[j]
            j -= 1
        my_list[j+1] = number_to_order
    return my_list
