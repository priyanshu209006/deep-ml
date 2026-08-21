def estimate_decode_latency(num_params, bytes_per_param, bandwidth_bytes_per_s):
    # Return [latency_ms, tokens_per_sec]
    bytes = num_params*bytes_per_param
    t = bytes/bandwidth_bytes_per_s
    t_ms = 1000*t
    token_ps = 1/t
    return [t_ms,token_ps]
    