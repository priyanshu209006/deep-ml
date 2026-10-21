
import numpy as np

def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
	pass
	classes,count = np.unique(y, return_counts= True)
	p_c = count/len(y)
	val = 1-np.sum(p_c**2)
	return round(val,3)