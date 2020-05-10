strings = "Hi, my name is Thiago!"

# approach 01
print(strings[::-1])

# approach 02
def reverseString(strings):
    for i in range(len(strings) - 1, -1, -1):
      print(strings[i], end='')

#approach 03
def reverseStringWithList(strings):
  newStrings = []
  for i in range(len(strings) - 1, -1, -1):
      newStrings.append(strings[i])
  return "".join(newStrings)

reverseString(strings)
print() # skip a new line
print(reverseStringWithList(strings))