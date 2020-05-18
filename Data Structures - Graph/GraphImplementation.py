class Graph():

	def __init__(self):
		self.numberOfNodes = 0
		self.adjacentList = {}

	def __str__(self):
		return str(self.__dict__)

	def addVertex(self, node):
		self.adjacentList[node] = []
		self.numberOfNodes += 1

	def addEdge(self, nodeA, nodeB):
		self.adjacentList[nodeA].append(nodeB)
		self.adjacentList[nodeB].append(nodeA)

	def showConnections(self):
		for x in self.adjacentList:
			print(x, end='-->')
			for i in self.adjacentList[x]:
				print(i, end=' ')
			print()

myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '3')
myGraph.addEdge('2', '3') 
myGraph.addEdge('2', '0') 
print(myGraph)
myGraph.showConnections()
