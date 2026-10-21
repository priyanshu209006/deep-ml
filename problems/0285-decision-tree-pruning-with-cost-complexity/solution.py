def compute_pruning_alphas(tree: dict) -> list:
    """
    Computes effective alpha values for cost-complexity pruning.
    
    Args:
        tree: Dictionary representing a decision tree node with keys:
              - 'samples': number of samples reaching this node
              - 'errors': misclassification count if node becomes a leaf
              - 'left': left child subtree (dict) or None
              - 'right': right child subtree (dict) or None
        
    Returns:
        List of effective alpha values for internal nodes, sorted ascending.
    """
    alphas = []
    def traverse(node):
        if node['left'] is None and node['right'] is None:
            return node['errors'],1
        left_err,left_count = traverse(node["left"])
        right_err, right_count = traverse(node["right"])
        error = (left_err+right_err)
        num_leaves = left_count+right_count
        alpha = (node['errors'] - error)/(num_leaves -1)
        alphas.append(alpha)
        return error,num_leaves
    traverse(tree)
    return alphas

    