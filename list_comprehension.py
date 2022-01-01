

if __name__ == "__main__":
	"""
	Transpose a matrix and
	some list comprehension
	"""

	matrix = [
		[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 11, 12]
	]

	print(matrix, "\n\n")

	new_matrix = []
	for col_index in range(4):
		new_row = []
		for row in matrix:
			new_row.append(row[col_index])
		new_matrix.append(new_row)

	print(new_matrix, "\n\n")

	# If a list comprehension has an intial expression of a list comprehension
	# The first LC will execute before the second iterates
	print(
			[
				[row[col_index] for row in matrix] for col_index in range(4)
			]
	)

	# A normal nested for loop works the same in a list comprehension
	print([row[col_index] for row in matrix for col_index in range(4)])
