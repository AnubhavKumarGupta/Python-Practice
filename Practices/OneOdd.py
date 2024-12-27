l = [4, 1, 2, 4, 5, 6, 4, 6, 7, 2, 5, 7, 8, 9]

# res = 0
# for i in l:
#     res = res ^ i
# print(l)


def getOddOccurrence(l):

	# Initialize result
	res = 0
	
	# Traverse the array
	for element in l:
		# XOR with the result
		res = res ^ element

	return res

# Test array
# arr = [ 2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]

print("%d" % getOddOccurrence(l))