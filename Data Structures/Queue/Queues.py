"""
FIFO (first in first out)

Like stacks, data can only be inserted at the end: this is called,'Enqueue'
Unlike stacks, data can only be removed from the head: this is called 'Dequeue'

OTHER kinds of Queues:
 - Doubly ended queues
 - Circular queues
 - Priority queues

USES:
 - storing printing tasks in a printer: docs are printed in the order they are recieved.
 - Applications where the ORDER of user requests matters
  - tickets to a concert
  - taxi services

 Implemented using a singly linked list Node Class
"""

class Node:
 def __init__(self, data):
  self.data = data
  self.next = None

class Queue:
	def __init__(self):
		self.head = None
		self.tail = None
	
	#pushes: O(1)
	def enqueue(self,data):
		new_node = Node(data)
		if self.head == None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node
	#pops: O(1)
	def dequeue(self):
		if self.head:
			current_node = self.head
			self.head = current_node.next
			current_node.next = None
			if self.head == None:
				self.tail = None
	
	# Checks if empty
	def has_elements(self) -> bool:
		return self.head != None

## Implementing a printer Queue

class PrinterTasks:
  def __init__(self):
    self.queue = Queue()
      
  def add_document(self, document):
    # Add the document to the queue
    self.queue.enqueue(document)
      
  def print_documents(self):
    # Iterate over the queue while it has elements
    while self.queue.has_elements():
      # Remove the document from the queue
      print("Printing", self.queue.dequeue())



# Queue and SimpleQueue classes in the queue module
import queue

orders_queue = queue.SimpleQueue()

#add elements to the queue:
orders_queue.put('Sushi')
orders_queue.put('Lasagna')
orders_queue.put('Paella')

print("The size is : ", orders_queue.qsize())

# remove elements from the queue:

print(orders_queue.get())
print(orders_queue.get())
print(orders_queue.get())

# check to see that we emptied the queue:
print("Empty quese: ", orders_queue.empty())

# manage restauraunt orders:
import queue

# Create the queue
my_orders_queue = queue.SimpleQueue()

# Add an element to the queue
my_orders_queue.put("samosas")

# Remove an element from the queue
my_orders_queue.get()