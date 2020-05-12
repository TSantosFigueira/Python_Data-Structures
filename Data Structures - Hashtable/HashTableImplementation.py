HASH_TABLE_SIZE = 50

class HashTable():

	def __init__(self):
		self.data = [None] * HASH_TABLE_SIZE

	def __str__(self):
		return str(self.__dict__)

	def hash(self, key):
		#Get the index of our array for a specific string key
		length = len(self.data)
		return hash(key) % length
	
	def set(self, key, value):
		index = self.hash(key)
		if self.data[index] is not None:
			# the index already contains values
			for key in self.data[index]:
				if key[0] == key:
					key[1] = value
					break
			else:
				# If no breaks was hit in the for loop, it 
        # means that no existing key was found, 
        # so we can simply just add it to the end.
				self.data[index].append([key, value])
		else:
			# This index is empty. We should initiate
			self.data[index] = []
			self.data[index].append([key, value])
	
	def get(self, key):
		# Get a value by KeyboardInterrupt
		index = self.hash(key)
		if self.data[index] is None:
			print("Key does not exist")
		else:
			#Loop through all key-value-pairs
			for keys in self.data[index]:
				if keys[0] == key:
					return keys[1]

			# If there is no return during the loop, key doesn't exist
			raise KeyError()


h = HashTable()
h.set('grapes',1000)
h.set('oranges', 200)
h.set('ichigo', 900)
h.set('meron', 400)

print(h.get('meron'))
print(h.get('grapes'))