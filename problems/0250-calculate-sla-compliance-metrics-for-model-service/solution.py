def calculate_sla_metrics(requests: list, latency_sla_ms: float = 100.0) -> dict:
    """
    Calculate SLA compliance metrics for a model serving endpoint.
    
    Args:
        requests: list of request results, each a dict with 'latency_ms' and 'status'
        latency_sla_ms: maximum acceptable latency in ms for SLA compliance
    
    Returns:
        dict with keys: 'latency_sla_compliance', 'error_rate', 'overall_sla_compliance'
        All values as percentages (0-100), rounded to 2 decimal places.
    """
    success = 0
    lat = 0
    error = 0
    timeout = 0
    for i in range(len(requests)):
        if requests[i]["status"] == "success":
            success = success+1
            if  float(requests[i]["latency_ms"]) <= latency_sla_ms:
                lat = lat+1
        elif requests[i]["status"] == "error":
            error = error+1
        else:
            timeout = timeout+1
    if len(requests)!=0:
        error_rate = 100*(error+timeout)/len(requests)
        latency_sla_compliance = (lat/success)*100 if success!=0 else 0
        overall_sla_compliance = 100*lat/len(requests)
        result = {
             "latency_sla_compliance": round(latency_sla_compliance,2),
             "error_rate": round(error_rate,2),
             "overall_sla_compliance": round(overall_sla_compliance,2)
        }

    return result if len(requests)!=0 else {}