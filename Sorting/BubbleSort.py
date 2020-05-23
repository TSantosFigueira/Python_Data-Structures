def BubbleSort(vector):
	i = 0
	while i < len(vector):
		for j in range(0, len(vector) - 1):
			if vector[j] > vector[j + 1]:
				aux = vector[i]
				vector[i] = vector[j]
				vector[j] = aux
		i += 1
	return vector


vector = [3, 6, 9, 1]
vector = BubbleSort(vector)
print(vector)
	