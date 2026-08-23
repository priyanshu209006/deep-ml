def calculate_covariance_matrix(vect: list[list[float]]) -> list[list[float]]:
	# Your code here
	def mean(feature):
		sum2=0
		for i in range(len(feature)):
			sum2 = sum2+feature[i]
		return sum2/len(feature)
	
	length = len(vect)
	
	
	def cova(vectors):
		sum1 = 0
		
		for i in range(len(vectors[0])):
			cov = 1
			for j in range(len(vectors)):
				cov = cov*(vectors[j][i]-mean(vectors[j]))
			sum1 = sum1 + cov
		
		return sum1/(len(vectors[0])-1)
	result = [[0 for _ in range(length)] for _ in range(length)]
	for i in range(length):
		for j in range(length):
			vectors = [vect[i], vect[j]]
			result[i][j] = cova(vectors)
	return result


