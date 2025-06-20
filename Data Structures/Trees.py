"""
top node is the ROOT

Further nodes are referred to as parents and children of other nodes.
     -----ROOT-----
     |             |
__parent__    __parent__
|         |   |        |
child  child child   child

Trees have levels. 

Binary tree:
 A tree where each node has 0, 1 or 2 children

USES:
storing heirarchical relationships
 - file system of a computer
 - HTMLdoc structure
 - In Chess, stores the possibel moves a rival player can make.
 - Used in many searching and sorting algoritms.
"""

# Binary Tree implementation

class TreeNode:

 def __init__(self, data, left= None, right= None):
  self.data = data
  self.left_child = left
  self.right_child = right

# building a tree:
node1 = TreeNode("B")
node2 = TreeNode("C")
root_node = TreeNode("A", node1, node2)