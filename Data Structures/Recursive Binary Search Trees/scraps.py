class TreeNode:

	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left_child = left
		self.right_child = right

class BinarySearchTree:
	def __init__(self, value):
		self.root = None

	def r_contains(self, value):
		return self.__r_contains(self.root, value)

	def __r_contains(self, current_node, value):
		if current_node == None:
			return False
		if value == current_node.value:
			return True 
		if value < current_node.value:
			return self.__r_contains(current_node.left, value)
		if value > current_node.value:
			return self.__r_contains(current_node.right, value)
	def r_insert(self, value):
		self.__r_insert(self.root, value)
	def __r_insert(self, current_node, value):
		if current_node == None:
			return TreeNode(value)
		if value < current_node.value:
			current_node.left = self.__r_insert(current_node.left, value) 
		if value > current_node.value:
			current_node.right = self.__r_insert(current_node.left, value)
		return current_node

my_tree = BinarySearchTree()
# my_tree.r_insert(2)
# my_tree.r_insert(1)
# my_tree.r_insert(3)