import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	a = np.array(A)
	t = np.array(T)
	s = np.array(S)
	if (s.shape[0]==s.shape[1] and t.shape[0]==t.shape[1]) and (np.linalg.det(t)!=0 and np.linalg.det(s)!=0):
		result = np.linalg.inv(t)@a@s
	else:
		return -1
	return result

