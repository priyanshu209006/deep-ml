import math

def softmax(scores: list[float]) -> list[float]:
    if not scores:
        return []
    
    max_score = max(scores)
    exp_scores = [math.exp(s - max_score) for s in scores]
    sum_exp = sum(exp_scores)
    
    return [e / sum_exp for e in exp_scores]
