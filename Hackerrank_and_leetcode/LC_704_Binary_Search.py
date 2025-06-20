import math
from typing import List


def search(nums, target) -> int:
	low = 0
	high = len(nums) - 1
	while low <= high:
		middle = (low + high) // 2
		if nums[middle] == target:
			return middle
		elif nums[middle] < target:
			low = middle + 1
		else:
			high = middle - 1
	return -1



assert search([-1, 0, 3, 5, 9, 12], 9) == 4
assert search([-1,0,3,5,9,12], 2) == -1
print("All assertions passed!!!")
