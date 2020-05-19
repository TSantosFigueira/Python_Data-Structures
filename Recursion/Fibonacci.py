def iterativeFibonacci(n):
	arr = [0, 1]
	for i in range(2, n + 1):
		arr.append(arr[i - 2] + arr[i - 1])
	return arr[n]

def recursiveFibonacci(n):
	if n < 2:
		return n
	return recursiveFibonacci(n - 1)  + recursiveFibonacci(n - 2) 


print(iterativeFibonacci(8))
print(recursiveFibonacci(8))
