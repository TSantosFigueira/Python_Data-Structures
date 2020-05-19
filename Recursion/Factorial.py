def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n - 1)

def iterativeFactorial(n):
	factorial = 1
	for i in range(n, 1, -1):
		factorial *= i
	return factorial

print(factorial(5))
#print(iterativeFactorial(5))