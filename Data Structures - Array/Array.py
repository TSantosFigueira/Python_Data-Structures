strings = ['a', 'b', 'c', 'd']

print(strings[2]) # O(1)

#push
strings.append('e') # O(1)

#pop
strings.pop()

#Add at first index
strings.insert(0, "x") # O(n)

#splice
strings.insert(2, 'x') # O(n)

print(strings)


