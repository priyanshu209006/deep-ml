import numpy as np
def solve_jacobi(a: np.ndarray, b: np.ndarray, n: int) -> list:
	[rows, cols] = np.shape(a)
	x = [0 for _ in range(cols)]
	r = [[0 for _ in range(rows)] for _ in range(cols)]
	d = [[0 for _ in range(rows)] for _ in range(cols)]
	for i in range(cols):
		for j in range(rows):
			if i==j:
				d[i][j] = a[i][j]
				r[i][j] = 0
			else:
				d[i][j] = 0
				r[i][j] = a[i][j]
	x_np = np.array(x)
	d_np = np.array(d)
	r_np = np.array(r)
	for i in range(n):
		x_np = np.linalg.inv(d_np)@(b - np.matmul(r_np,x_np))
		

	
	return np.round(x_np,4)