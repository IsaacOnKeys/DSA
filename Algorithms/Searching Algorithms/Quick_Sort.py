"""
Quicksort follows the divide and conquer principle.
- It uses a partition technique by choosing a value from the list called the pivot. All items smaller than the pivot will end at the left of the pivot, and greater elements at the right. Quicksort will be called recursively on the elements to the left and right of the pivot. 
--------------------------------------
Hoare's partition approach:
- set the pivot as the first element. 
- We use two pointers. The left pointer points to the first value from the pivot and the right pointer to the last value. 
- Move the left pointer until we find a greater value than the pivot.
- Continue with the right pointer and move it until we find a value lower than the pivot.
- Stop the right pointer and swap these items. 
- Start over again, movign the left pointer and stoppiong when we find a greater element.
We move
12. Quicksort - in action

the right pointer until we find a smaller value. When the pointers cross,
13. Quicksort - in action

we swap the item of the right pointer with the pivot.
14. Quicksort - in action

Now, the pivot is
15. Quicksort - in action

in its correct position. Elements to the left of the pivot are smaller than the pivot, and elements to the right are greater. We then apply quicksort to the left and right parts of the pivot.
- Starting with the left part, we select a new pivot and set the pointers. In this case, both pointers point to the same number. Since there aren't more numbers, we swap these items.
- Now, four is in its correct position. There is only one number left, so we leave it as is.
Once the left part is sorted, we continue with the right.
We select a new pivot and set the pointers. The left pointer points to a value that is greater than the pivot, so we stop.
-We move the right pointer to find a lower value. Since there isn't any, we finish pointing to the pivot, so we stop the right pointer and leave the pivot where it is.
- We continue with the last element. Since it is lower than the pivot, we swap it with the pivot.
The numbers are sorted. 
"""
# Implementation: First we implement the partition funtion, then we implement the quicksort function that calls the partition function.


def partition(my_list, first_index, last_index):
    pivot = my_list[first_index]
    left_pointer = first_index + 1
    right_pointer = last_index

    while True:
        # Iterate until the value pointed by left_pointer is greater than pivot or left_pointer is greater than last_index
        while pivot < left_pointer and last_index < left_pointer:
            left_pointer += 1

        while my_list[right_pointer] > pivot and right_pointer >= first_index:
            right_pointer -= 1
        if left_pointer >= right_pointer:
            break
        # Swap the values for the elements located at the left_pointer and right_pointer
        my_list[left_pointer], my_list[right_pointer] = my_list[right_pointer],  my_list[left_pointer]

    my_list[first_index], my_list[right_pointer] = my_list[right_pointer], my_list[first_index]
    return right_pointer


def quicksort(my_list, first_index, last_index):
    if first_index < last_index:
        # Call the partition() function with the appropriate parameters
        partition_index = partition(my_list, first_index, last_index)
        # Call quicksort() on the elements to the left of the partition
        quicksort(my_list, first_index, partition_index)
        quicksort(my_list, partition_index + 1, last_index)


my_list = [6, 2, 9, 7]
quicksort(my_list, 0, len(my_list) - 1)
print(my_list)
