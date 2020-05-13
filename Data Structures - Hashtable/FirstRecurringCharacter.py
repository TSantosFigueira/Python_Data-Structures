#given an array = [2,5,1,2,3,5,1,2,4]
# find the first recurrent element
# expected output: 2

#first approach / naive approach O(n)
def FindRecurrent(myList):
	for i in range(0, len(myList)):
		for j in range(i + 1, len(myList)):
			if(myList[i] == myList[j]):
				return myList[i]
	return -1

#hash table approach
def FindRecurrentWithHashtable(mylist):
	myDict = {}
	for i in range(0, len(mylist)):
		if(mylist[i] in myDict):
			return mylist[i]
		else:
			myDict[mylist[i]] = i
	return -1

mylist = [2,5,1,2,3,5,1,2,4]
x = FindRecurrentWithHashtable(mylist)
print(x)