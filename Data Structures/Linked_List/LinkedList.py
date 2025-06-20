class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node
        #length is an attribute, not a method!!!!!
        self.length = 1
    
    def print_list(self):
        temp = self.head
        if temp is None:
            print(None)
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        # True is going to be used by another method later, not necessary otherwise
        return True
    def pop(self):
        # start with handling an empty list
        if self.length == 0:
            return None 
        #point both at head
        pre = self.head
        temp = self.head
        #make them iterate until the end of the list, leaving pre 1 behind
        while temp.next is not None:
            pre = temp
            temp = temp.next
        #reset the tail one step where pre is    
        self.tail = pre
        #it's necessary to 'break off' last node
        self.tail.next = None
        self.length -= 1
        # If list is 0, or 0 AFTER starting with at least 1 and decrementing by 1- the latter being why it is at the end.
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp 
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail == None
        return temp
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    def find_middle_node(self):
        temp = self.head
        pre = self.head
        while temp and temp.next:
            pre = pre.next
            temp = temp.next
            temp = temp.next
        return pre.value

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)
my_linked_list.append(9)

my_linked_list.print_list()
my_linked_list.find_middle_node()
