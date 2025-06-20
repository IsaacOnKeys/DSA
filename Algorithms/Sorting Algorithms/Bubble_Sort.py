"""
Bubble Sort:
 1. start by comparing the first 2 items in a collection. If the first one is greater than the second, swap them.
 2. Move up through the indices, repeating the operation.
 3. When you finish, start over at the beginning.
 4. move up through the collection, but not the last as it is already sorted.
 5. Repeat this, each time moving up through an increasingly shorter list.

-----------------------------
Complexity of O(n^2)
Average case of Theta(n^2)
Dosen't perform well with highly unsorted large lists.
Ideal for large, but sorted or almost sorted because of it's Theta (average) complexity. Also good for small lists.


"""
# Implementation of Bubble sort with a nested loop
# Complexity of O(n^2)
# Best case, when list is already sorted: Omega(n^2)


def bubble_sort(my_list):
    list_length = len(my_list)
    # outer loop iterates as many times as the length of list.
    for i in range(list_length - 1):
        # subtract i to avoid checking the values at the end of the list.
        for j in range(list_length - 1 - i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list


# Try it out!
print(bubble_sort([4, 3, 7, 1, 5]))

# Using an outer while loop with a for loop:
# Complexity of O(n^2)
# Best case, when list is already sorted: Omega(n)


def bubble_sort(my_list):
    list_length = len(my_list)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(list_length-1):
            if my_list[i] > my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                is_sorted = False
        list_length -= 1
    return my_list
