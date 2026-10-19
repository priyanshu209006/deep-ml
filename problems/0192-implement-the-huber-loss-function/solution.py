import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
	"""
	Compute the Huber Loss between true and predicted values.

	Args:
		y_true (float | list[float]): Ground truth values
		y_pred (float | list[float]): Predicted values
		delta (float): Transition threshold between MSE and MAE behavior

	Returns:
		float: Average Huber loss
	"""
	# Your code here
	res = np.array(y_pred)-np.array(y_true)
	loss = np.where(np.abs(res)<=delta, 0.5*(res)**2, delta*(np.abs(res) - 0.5*delta) )
	huber = np.mean(loss)
	return huber