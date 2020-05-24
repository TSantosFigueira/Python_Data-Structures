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

	def breadthFirstSearch(self):
		current = self.root
		mylist = []
		queue = []
		queue.append(current)

		while len(queue) > 0:
			current = queue[0]
			del queue[0]
			mylist.append(current.data)
			if current.left:
				queue.append(current.left)
			if current.right:
				queue.append(current.right)

		return mylist

	def recursiveBreadthFirstSearch(self, queue, myList):
		if len(queue) == 0:
			return myList
		currnode = queue[0]
		del queue[0]
		myList.append(currnode.data)
		if currnode.left:
			queue.append(currnode.left)
		if currnode.right:
			queue.append(currnode.right)

		return self.recursiveBreadthFirstSearch(queue, myList)

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

x = tree.lookup(170)
print(x)  
print(tree.breadthFirstSearch())
print(tree.recursiveBreadthFirstSearch([tree.root],[]))
			