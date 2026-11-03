import numpy as np
def precision(y_true, y_pred):
	# Your code here
	if (y_true==1).sum() == 0:
		return 0
	tp = ((y_true == 1) & (y_pred==1)).sum()
	fp = ((y_true == 0) & (y_pred==1)).sum()
	return tp/(tp+fp)