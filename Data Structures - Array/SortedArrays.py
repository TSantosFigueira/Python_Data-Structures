array1 = [0, 3, 4, 31]
array2 = [4, 6, 3]

#approach 01 - naive approach
def MergeSortedArrays(array1, array2):
	for i in range(len(array2)):
		array1.append(array2[i])
	return sorted(array1)

def MergeArrays(array1, array2):
	sortedArray = []

	i = 0
	j = 0

	while(i < len(array1) and j < len(array2)):
		if(array1[i] <= array2[j]):
			sortedArray.append(array1[i])
			i += 1
		elif(array2[j] < array1[i]):
			sortedArray.append(array2[j])
			j += 1

	return sortedArray + array1[i:] + array2[j:]
		

#print(MergeSortedArrays(array1, array2))
print(MergeArrays(array1, array2))

