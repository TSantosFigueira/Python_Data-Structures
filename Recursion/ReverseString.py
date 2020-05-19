def reverse(word):
	length = len(word)
	if(length == 0):
		return 
	last_char = word[length - 1]
	print(last_char, end=' ')
	reverse(word[0:length - 1])

reverse("Hello there!")
