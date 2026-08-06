import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	b = []
	x=0
	reshaped_matrix = np.zeros(new_shape)
	for i in range(len(a)):
		for j in range(len(a[i])):
			b.append(a[i][j])
	if new_shape[0]*new_shape[1] == len(b):
		for k in range(new_shape[0]):
			for l in range(new_shape[1]):
				reshaped_matrix[k][l] = b[x]
				x+=1
		return reshaped_matrix
	else:
		return []