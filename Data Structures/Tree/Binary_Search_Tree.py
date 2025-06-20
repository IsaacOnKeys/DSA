"""
In a binary search tree, the left node can only contain a value lower than the parent, and the right node can only hold values higher than the parent. 
-------------------------------
Uses:
- Order lists efficiently
- Much faster at searching than arrays and linked lists.
- Used for implementing more complex data structures:
  - Dynamic Sets
  - Lookup Table
  - Priority Queues

---------------------------
Traversal Of Trees:
process of visting all Nodes of a tree

Depth First Search (DFS): allows you to traverse a tree.

Binary Trees: There are 3 ways to traverse a binary tree with DFS:
 In-Order:
  order: Left -> Current -> Right Complexity = O(n)
		Used for: to obtain the node's values in ascending order
 Pre-Order
  order: Current -> Left --> Right Complexity = O(n)
		Used for: 
			- create a copy of a tree
			- get prefix expressions
 Post-Order 
  order: Left -> Right -> Current Complexity = O(n)
		Used for: 
			- Deleting Binary Trees
			- to get Postfix Expressions

Breadth First Search:
Starting from the top, the BFS algo. searches all nodes at each level of the tree before moving down to the next level 

"""

### Binary Seach Tree implementation ###

# Start with a tree node class


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right


class BinarySearchTree:
    def __init__(self):
        self.root = None
    ## Implementing the Search algorithm ##

    def search(self, search_value):
        current_node = self.root
        while current_node:
            if search_value == current_node.data:
                return True
            elif search_value < current_node.data:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
    # If the loop ends without finding the search_value:
        return False

    def insert(self, data):
        # first create a node with the data
        new_node = TreeNode(data)
        # if the tree doesn't have a root node, the new node is the root, and execution finishes
        if self.root == None:
            self.root = new_node
            return
        # if the node has a root
        else:
            current_node = self.root
            while True:
                if data < current_node.data:
                    if current_node.left_child == None:
                        current_node.left_child = new_node
                        return
                    else:
                        current_node = current_node.left_child
                elif data > current_node.data:
                    if current_node.right_child == None:
                        current_node.right_child = new_node
                        return
                    else:
                        current_node = current_node.right_child

    def find_min(self):
        # Set current_node as the root
        current_node = self.root
        # Iterate over the nodes of the appropriate subtree
        while current_node.left_child:
            # Update current_node
            current_node = current_node.left_child
        return current_node.data

# Depth First Traversal: In order style
    def in_order(self, current_node):
        if current_node:
            self.in_order(current_node.left_child)
            print(current_node.data)
            self.in_order(current_node.right_child)


# Pre-Order traversal

    def pre_order(self, current_node):
        if current_node:
            print(current_node.data)
            self.pre_order(current_node.left_child)
            self.pre_order(current_node.right_child)

#
