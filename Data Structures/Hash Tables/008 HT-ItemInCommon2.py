"""
More efficient implementation. This is because it uses 2 for loops, separately, un-nested. so that is O(2n)m which simplifies to O(n).
"""


def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True

    return False


list1 = [1, 3, 5]
list2 = [2, 4, 5]


print(item_in_common(list1, list2))
