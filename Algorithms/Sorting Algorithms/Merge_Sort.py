"""
Merge Sort: follows the divide and conquer strategy.
 1. Divide the problem into smaller problems
 2. Sub problems are solved recursively, then combined into the final solution.

 STEPS: divide the list in half, and those halves in half, etc, then recombine from bottom up sorting as you go into a new list.
 --------------------
COMPLEXITY
 Worst, Average, and Best
 O(n log n) # faster than bubble, selection, and insertion sort
- Suitable for large lists of numbers
Other bubble =  insertion have better best case complexity
DOOOOWN side:
Space complexity: O(n) because of recursion
Other algos have space complexity of O(1)

??? Solved with memoization?!?!?
"""

# Merge Sort implementaion:


def merge_sort(my_list):
    if len(my_list) > 1:
        # divide the list into 2 parts:
        mid = len(my_list) // 2
        left_half = my_list[:mid]
        right_half = my_list[mid:]

        # call merge_sort recursively until each list has only 1 element:
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted parts:
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]
                i += 1
            else:
                my_list[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            my_list[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            my_list[k] = right_half[j]
            j += 1
            k += 1


new_list = [35, 22, 90, 4, 50, 20, 30, 40, 1]
merge_sort(new_list)
print(new_list)
