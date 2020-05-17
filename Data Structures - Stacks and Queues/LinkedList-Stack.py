class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:

	def __init__(self):
		self.top = None
		self.bottom = None
		self.length = 0

	def peek(self):
		return self.top.data

	def push(self, data):
		new_data = Node(data)
		if(self.length == 0):
			self.top = new_data
			self.bottom = new_data
		else:
			self.top.next = new_data
			self.top = new_data
		self.length += 1		

	def pop(self):
		if(self.length <= 0):
			return -1
		else:
			i = 1
			current = self.bottom
			while( i != self.length - 1):
				current = current.next
				i += 1
			popped_element = self.top
			current.next = None
			self.top = current
			self.length -= 1
			return popped_element.data

	def printStack(self):
		current = self.bottom
		while current != None:
			print(current.data, end = ', ')
			current = current.next
		print()


s = Stack()
s.push(9)
s.push(5)
s.push(16)
s.push(18)
s.printStack()
s.pop()
s.printStack()
