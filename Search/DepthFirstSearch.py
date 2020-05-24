class Node():
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

class BinarySearchTree():
	def __init__(self):
		self.root = None

	def insert(self, data):
		new_node = Node(data)
		if self.root == None:
			self.root = new_node
			return
		else:
			current_node = self.root
			while True:
				if data < current_node.data:
					#lef
					if current_node.left == None:
						current_node.left = new_node
						return
					else:
						current_node = current_node.left
				elif data > current_node.data:
					#right
					if current_node.right == None:
						current_node.right = new_node
						return
					else:
						current_node = current_node.right

	def lookup(self, data):
		current_node = self.root
		while True:
			if current_node == None:
				return False
			if data == current_node.data:
				return True
			elif data < current_node.data:
				current_node = current_node.left
			else:
				current_node = current_node.right

	def printTree(self):
		if self.root != None:
			self.printt(self.root)

	def printt(self, current_node):
		if current_node != None:
			self.printt(current_node.left)
			print(str(current_node.data))
			self.printt(current_node.right)

	def inorder(self, currentNode, myList):
		if currentNode != None:
			self.inorder(currentNode.left, myList)
			myList.append(currentNode.data)
			self.inorder(currentNode.right, myList)
		return myList

	def preorder(self, currenNode, myList):
		if currenNode != None:
			myList.append(currenNode.data)
			self.preorder(currenNode.left, myList)
			self.preorder(currenNode.right, myList)
		return myList

	def postorder(self, currentNode, myList):
		if currentNode.left:
			self.postorder(currentNode.left, myList)
		if currentNode.right:
			self.postorder(currentNode.right, myList)
		myList.append(currentNode.data)
		return myList
		

	
tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(tree.inorder(tree.root,[]))
print(tree.preorder(tree.root,[]))
print(tree.postorder(tree.root,[]))
