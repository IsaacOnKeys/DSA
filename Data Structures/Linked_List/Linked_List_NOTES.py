'''
Structure of a linked list:
Head node, Tail node, all nodes in between point to the next, and the last node points to 'none'. All nodes are pointers.

MEMORY
------------
The nodes are spread out, almost randomly in Memory, and are only able to be referenced by the previous node which points at it.

LIST vs LINKED LIST
--------------------
list nodes are in a contiguous place in memory, so an index can be applied. Each index then maps to a specific address in memory.

METHODS & BIG O
------
Append(): O(1)
	Why? There is already a pointer available (the last node) for the node you want to append, so you simply add it, and set it to 'tail'. 

Pop(): O(n)
	Why? When you remove the end node, the 'tail' node is left hanging, but it needs to point at the new end node. To do this, you need to iterate through the whole list in order to find the last node in the list.

Prepend(): O(1)
	Why? You just need to point it at the head node, then set it as the head, every time.

Push(): O(1)
	Why? just need to use head = head.next(), ant removes the old head.

Insert(): O(n)
	Why? Can only find specific nodes by value, since there is no index. Start at the head, and iterate through the list until you find the value you want to insert in front of.
When you find the value, you want your new node to point at the node after the value you searched for.
So set new node Equal to value node, which points it at the right node, now opint the value node at your inserted node.

Remove(): O(n)
	Why? we want to remove node A. Iterate throught the list until you find the value A. Set the node pointing at A (B) = A, then A can be removed.

Lookup_by_value(): O(n)
	Why? Simply iterate throught the list until you find what you are looking for.

Lookup_by_index(): O(n)
	Why? Since there is no set index, you have to count the nodes as you go to ascertain the index, so iterating throught the list is necessary.

Long Winded Explanation
--------
Each element is called a node and has two parts. The first part is the data. The second part is a pointer to the next node. The last link points to null. The first node is the head, and the final node is the tail.

This data doesn't need to be stored in contiguous blocks of memory, so it can be located in any available memory address.If each node has one link, it is called a singly linked list. If each node has two links in either direction, it is called a doubly linked list. We'll focus on singly linked lists. 

Linked lists can be used to implement other data structures like stacks, queues, and graphs. A common application of a linked list is to access information by navigating backward and forward, such as on a web browser or music playlist. 


Each node can be stored in a seperate location in memory, connect by a address reference.
singly linked lists:
	BreadSteps():
		mix -> rest -> shape -> bake

doubly linked list:
	Web Browser:
		Page1 --> <-- Page2 --> <--Page3
		
Linked lists can be used to implement other data structures, like:
	- stacks
	- queues
	- graphs

A linked list is used to access information forwards and backwards, like in a Web Browser, or music playlist.

Creating a linked list Class comprised of with a Node class. The data attribute contains the value of the node, and the next points to the next node. Initially it will point to None. The Linked list will contain methods to insert or remove nodes at the beginning, end, or given position, and to search the for a value in the list.
'''

""" Node is both a value and a pointer. It is essentially a dictionary :
{
	"value":4,
	"next":None
}
So a linked list [1,2,3], would look like this:
my_ll = head = {
															"value":1,
															"next": {
																								"value":2,
									tail---------> "next":{
																																"value":3,
																																"next": None
																																}
																							}
															}
So if want to access 3, I would use:
>>> print(my_ll[head]["next"]["next"]["value"])
OR
>>> print(my_ll.head.next.next.value)
"""

# node is a value + pointer, in a linked list.
# head: 1-> 2-> tail: 3 -None
#######################################
# Linked List Implementation style 1: #
#######################################


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    # def return_list(self):
    #     temp = self.head
    #     while temp is not None:
    #         return temp.value
    #         temp = temp.next
# Append steps:
# Create a new node
# last item point to new node
# tail point to new node
# edge case when the list is empty

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        # increment the ATTRIBUTE length
        self.length += 1
        # True statement will be used by another method later
        return True


# create a new linked list:
my_linked_list = LinkedList(4)
my_linked_list.append(5)

# print(f"The length of my list is: {my_linked_list.length} \n It contains these values: {}")
my_linked_list.print_list()

#####################################################
# Linked list Implementation style 2 from DataCamp: #
#####################################################

"""
class Node2:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node2(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node2(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def remove_at_beginning(self):
        # The "next" node of the head becomes the new head node
        self.head = self.head.next

    # Searches for a given value in the LL
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        # return false if data is not found
        return False


# Implement a new Linked List
sushi_preparation = LinkedList2()
# add nodes at beginning and end
sushi_preparation.insert_at_end("prepare")
sushi_preparation.insert_at_end("roll")
sushi_preparation.insert_at_beginning("assemble")
# search for a value
print(sushi_preparation.search("roll"))  # returns True
print(sushi_preparation.search("mixing"))  # returns False
"""
