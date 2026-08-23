def compute_receptive_field(input_size, layers):
    # Initial state (Layer 0: the raw input)
    r = 1  # Receptive field starts at 1 pixel
    j = 1  # Jump starts at 1 pixel
    n = input_size
    
    for kernel_size, stride, padding in layers:
        # 1. Update the receptive field
        r = r + (kernel_size - 1) * j
        
        # 2. Update the jump distance
        j = j * stride
        
        # 3. Update the spatial output size
        n = (n + 2 * padding - kernel_size) // stride + 1
        
    return {
        'receptive_field': r,
        'output_size': n
    }

