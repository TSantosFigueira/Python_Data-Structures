class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class Queue:

	def __init__(self):
		self.first = None
		self.last = None
		self.length = 0

	def peek(self):
		return self.first.data

	def enqueue(self, data):
		new_data = Node(data)
		if(self.length == 0):
			self.first = new_data
			self.last = new_data
		else:
			self.last.next = new_data
			self.last = new_data
		self.length += 1		

	def dequeue(self):
		if(self.length <= 0):
			return -1
		else:
			temp = self.first.next
			removed_element = self.first
			if temp == None:
				self.first = None
			else:
				self.first.next = None
				self.first = temp
			self.length -= 1
			return removed_element.data

	def printQueue(self):
		current = self.first
		while current != None:
			print(current.data, end = ', ')
			current = current.next
		print()

myq = Queue()
myq.enqueue('google')
myq.enqueue('microsoft')
myq.enqueue('facebook')
myq.enqueue('apple')
myq.printQueue()
myq.dequeue()
myq.printQueue()
myq.dequeue()
myq.printQueue()