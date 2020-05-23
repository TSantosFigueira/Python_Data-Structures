def InsertionSort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1
		while j >= 0 and arr[j] > key:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key

arr = [12, 11, 13, 5, 6] 
InsertionSort(arr)

#[11, 12, 13, 5, 6] J = 0  I = 1
#[11, 12, 13, 5, 6] J = 1  I = 2
#[11, 12, 13, 5, 6] J = 2  I = 3
#[5, 11, 12, 13, 6] J = 3 I = 4
#[5, 11, 12, 13, 13]  J = 2
#[5, 11, 12, 12, 13] j = 1
#[5, 11, 11, 12, 13] j = 0
#[5, 6, 12, 12, 13]

for i in range(len(arr)): 
  print ("%d" %arr[i])
