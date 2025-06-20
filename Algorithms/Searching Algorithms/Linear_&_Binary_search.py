"""
Linear search tries to search for a value by looping through each element of an list.
-for unordered lists, otherwise, use binary search.
- Complexity of linear search= O(n) IOW, the worst case scenerio is the length of the list.

Binary search: improves the time time complexity of a linear search.
- Only applies to ordered lists.
- Complexity of binary search: O(log n)
"""

def linear_search(unordered_list, search_value):
 #loop throught the list, and return True if the value is found
 for index in range(len(unordered_list)):
  if unordered_list[index] == search_value:
   return True
#If the value is not found, return False
 return False

ordered_list = [2,5,10,12,15,17,20]

def binary_search(ordered_list, search_value):
   # set to first position of the list
   first = 0
   # set to last position of the list
   last = len(ordered_list) - 1

   while first <= last:
      middle = (first + last) // 2 # '//' = floor division
#Tracking the algorithm:
      print(f'first = {first}')
      print(f'last = {last}')
      print(f'middle = {middle}')

      if search_value == ordered_list[middle]:
         return print(f'the number {search_value} was found at index {middle}')
      elif search_value < ordered_list[middle]:
         last = middle - 1
      else:
         first = middle + 1

binary_search(ordered_list,5)

#### Binary Search -- Recursive Algorithm ####

def binary_search_recursive(ordered_list, search_value):
  # Define the base case
  if len(ordered_list) == 0:
    return False
  else:
    middle = len(ordered_list)//2
    # Check whether the search value equals the value in the middle
    if search_value == ordered_list[middle]:
        return True
    elif search_value < ordered_list[middle]:
        # Call recursively with the left half of the list
        return binary_search_recursive(ordered_list[:middle], search_value)
    else:
        # Call recursively with the right half of the list
        return binary_search_recursive(ordered_list[:middle -1], search_value)
  
print(binary_search_recursive([1,5,8,9,15,20,70,72], 5))

