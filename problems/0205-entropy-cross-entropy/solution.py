import numpy as np

def entropy_and_cross_entropy(P: list[float], Q: list[float]) -> tuple[float, float]:
	"""
	Compute entropy of P and cross-entropy between P and Q.
	
	Args:
		P: True probability distribution
		Q: Predicted probability distribution
	
	Returns:
		Tuple of (entropy H(P), cross-entropy H(P,Q))
	"""
	# Your code here
	p_np = np.array(P)
	q_np = np.array(Q)
	H_p = -np.sum(np.where(p_np==0, 0,(p_np*np.log(p_np)))) 
	H_p_q = -np.sum(np.where((p_np>0)&(q_np==0), float('inf'),(p_np*np.log(q_np)))) 
	return H_p,H_p_q

	pass