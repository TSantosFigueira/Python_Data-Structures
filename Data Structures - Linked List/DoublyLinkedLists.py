# 3 --> 8 --> 5

class Node():
	def __init__(self, data):
		self.data = data
		self.next = None
		self.previous = None

class LinkedList():
	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, data):
		new_node = Node(data)
		if(self.head == None):
			self.head = new_node
			self.tail = new_node
			self.length = 1
		else:
			self.tail.next = new_node
			new_node.previous = self.tail
			self.tail = new_node
			self.length += 1

	def prepend(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head.previous = new_node
		self.head = new_node
		self.length += 1

	def insertAt(self, index, data):
		new_node = Node(data)	
		if index >= self.length:
			self.append(data)
			return
		if index == 0:
			self.prepend(data)
			return
		else:
			leader = self.traverseToIndex(index - 1)
			temp = leader.next
			leader.next = new_node
			new_node.next = temp
			new_node.previous = leader
			temp.previous = new_node
			self.length += 1

	def removeAt(self, index):
		if index > self.length:
			print("Out of bounds")
			return

		if index == 0:
			self.head = self.head.next
			self.length -= 1
			return
		# last element of the linked list
		if index == self.length - 1:
			 self.tail = self.tail.previous
			 self.tail.next = None
			 self.length -= 1
			 return
		
		leader = self.traverseToIndex(index - 1)
		unwanted_node = leader.next
		temp = unwanted_node.next
		leader.next = temp
		temp.previous = leader
		self.length -= 1

	def traverseToIndex(self, index):
		temp = self.head
		i = 0
		while i != index:
			temp = temp.next
			i += 1
		return temp

	def printLinkedList(self):
		temp = self.head
		while temp != None:
			print(temp.data, end=', ')
			temp = temp.next
		print()
		print('Length = ', self.length)			


l = LinkedList()
l.append(10)
l.append(5)
l.append(6)
l.insertAt(1, 99)
l.printLinkedList()



		