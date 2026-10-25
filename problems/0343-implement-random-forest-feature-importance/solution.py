import pandas as pd
def random_forest_feature_importance(trees: list, n_features: int) -> list:
    """
    Calculate feature importance from a random forest using Mean Decrease in Impurity.
    
    Args:
        trees: List of trees, where each tree is a list of node splits.
               Each split is a dict with:
               - 'feature_index': int, the feature used for splitting
               - 'impurity_decrease': float, the weighted impurity decrease
        n_features: Total number of features in the dataset
    
    Returns:
        List of feature importances normalized to sum to 1.0
    """
    importance = [0.0] * n_features

    for tree in trees:
        for node in tree:
            importance[node["feature_index"]] += node["impurity_decrease"]

    total = sum(importance)

    if total > 0:
        importance = [x/total for x in importance]

    return importance