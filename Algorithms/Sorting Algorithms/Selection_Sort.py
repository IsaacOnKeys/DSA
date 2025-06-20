"""
Selection Sort:
 1. move up the list, always looking for the lowest vale, and keeping track of it until the end of the list.
 2. When we reach the end we swap the lowest value with the first unordered value.
 ---------------------------
 Complexity
 n^2 in Worst, average and Best cases
"""

# Selection Sort implementation


def selection_sort(my_list):
    list_length = len(my_list)
    for i in range(list_length - 1):
        # save the first value as the lowest value:
        lowest = my_list[i]
        # record the index.
        index = i
        for j in range(i + 1, list_length):
            if my_list[j] < lowest:
                index = j
                lowest = my_list[j]
        my_list[i], my_list[index] = my_list[index], my_list[i]
    return my_list
