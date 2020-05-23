def SelectionSort(array):
	# Traverse through all array elements 
	for i in range(len(array)):
		# Find the minimum element in remaining  
    # unsorted array 
		min_idx = i
		for j in range(i+1, len(array)):
			if array[min_idx] > array[j]:
				min_idx = j
		# Swap the found minimum element with  
		# the first element  
		array[i], array[min_idx] = array[min_idx], array[i] 
	return array	
			
array = [24, 6, 2, 9, 0, 7]
print(SelectionSort(array))