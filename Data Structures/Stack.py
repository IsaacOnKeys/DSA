"""
FIFO: First in First out

Based on a linked list: using the same NODE Class to store the value

Attributes:

data: contains the data assigned to the Node
size: keeps track of 'height' of the stack. incremented +1 with push(), decremented -1 with pop()
top: assigned to the top Node, or last-in Node which is accessible.
METHODS

push: adds a new Node
pop: removes a Node and returns it's value
peek: returns a Node's value without removind the Node

Note:
- these methods are all O(1), making them super fast
- stacks are good for undo (ctr+z) functions, and matching bracket checking -> {[()]} 


"""
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.top = None
    self.size = 0
    
  def push(self, data): #O(1)
    # Create a node with the data
    new_node = Node(data)
    if self.top:
      new_node.next = self.top
    # Set the created node to the top node
    self.top = new_node
    # Increase the size of the stack by one
    self.size += 1
  def pop(self): #O(1)
     # Check if there is a top element
     if self.top is None:
       return None
     else:
       popped_node = self.top
       # Decrement the size of the stack
       self.size -= 1
       # Update the new value for the top node
       self.top = self.top.next
       popped_node.next = None
       return popped_node.data 

# The queue.py library contains a stack Class called LifoQueue

# Import the module to work with Python's LifoQueue
import queue

# Create an infinite LifoQueue
my_book_stack = queue.LifoQueue(maxsize=0)

# Add an element to the stack
my_book_stack.put("Don Quixote")

# Remove an element from the stack
my_book_stack.get()