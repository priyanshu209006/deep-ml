def calculate_batch_health(predictions: list, confidence_threshold: float = 0.5) -> dict:
    """
    Calculate health metrics for a batch prediction job.
    
    Args:
        predictions: list of prediction results, each a dict with 'status' and optionally 'confidence'
        confidence_threshold: threshold below which a prediction is considered low confidence
    
    Returns:
        dict with keys: 'success_rate', 'avg_confidence', 'low_confidence_rate'
        All values as percentages (0-100), rounded to 2 decimal places.
    """
    suc = 0
    total = 0
    err = 0
    less = 0

    for i in range(len(predictions)):
        if predictions[i].get("status")=="success":
            suc = suc+1
            total = total+predictions[i].get("confidence")
            if float(predictions[i].get("confidence")) < confidence_threshold:
                less = less+1
    if len(predictions)!=0:
        result = {
        "success_rate": round(100*suc/len(predictions),2) if suc!=0 else 0,
        "avg_confidence":round(100*total/suc,2) if suc!=0 else 0,
        "low_confidence_rate": round(100*less/suc,2) if suc!=0 else 0
        }
        return result
    else:
        return {}
