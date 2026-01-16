"""
That code manually implements a min-heap–based priority queue:

self.heap stores elements as a list (a binary tree in array form).

push() adds an element and calls _bubble_up() to restore heap order by comparing with parents and swapping upward if smaller.

pop() removes the smallest element (root). It swaps it with the last element, removes the last, then calls _bubble_down() to restore order downward.

_bubble_up() moves a newly added element up until its parent is smaller.

_bubble_down() moves a displaced element down until both children are larger.

_swap() exchanges two elements in the list.

This keeps the smallest element at index 0, enabling O(1) access and O(log n) insert/remove.

"""
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        value = self.heap.pop()
        self._bubble_down(0)
        return value

    def _bubble_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self._swap(index, parent)
            index = parent
            parent = (index - 1) // 2

    def _bubble_down(self, index):
        n = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == index:
                break
            self._swap(index, smallest)
            index = smallest

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
