# 3 --> 8 --> 5

class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

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
			self.tail = new_node
			self.length += 1

	def prepend(self, data):
		new_node = Node(data)
		self.head.next = new_node
		self.head = new_node
		self.length += 1

	def insertAt(self, index, data):
		new_node = Node(data)
		i = 0
		temp = self.head
		
		if index >= self.length:
			self.append(data)
			return
		if index == 0:
			self.prepend(data)
			return
		
		while i < self.length:
			if i == index - 1:
				temp.next, new_node.next = new_node, temp.next
				self.length += 1
				break
			temp = temp.next
			i += 1

	def removeAt(self, index):
		temp = self.head
		i = 0

		if index > self.length:
			print("Out of bounds")
			return

		if index == 0:
			self.head = self.head.next
			self.length -= 1
			return

		while(i < self.length):
			# last element of the linked list
			if i == self.length - 1:
				temp.next = None
				self.tai = temp
				self.length -= 1
				break
			# found element to delete
			if i == index - 1:
				temp.next = temp.next.next
				self.length -= 1
				break
			i += 1
			temp = temp.next

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
l.removeAt(0)
l.printLinkedList()



		