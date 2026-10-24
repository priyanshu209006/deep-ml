import math
import numpy as np
from collections import Counter

def calculate_entropy(labels: list) -> float:
    """Calculate the entropy of a list of labels."""
    # Your code here
    if len(labels)==0:
        return 0
    classes, count = np.unique(labels, return_counts =True)
    p_c = count/len(labels)
    return np.sum(-np.array(p_c)*np.log2(np.array(p_c)))
    

def calculate_information_gain(examples: list[dict], attr: str, target_attr: str) -> float:
    """Calculate the information gain of splitting on attr."""
    X_l = []
    y_l = []
    for i in range(len(examples)):
        X_l.append(examples[i][attr])
        y_l.append(examples[i][target_attr])
    
    parent_entropy = calculate_entropy(y_l)
    X = np.array(X_l)
    y = np.array(y_l)
    classes = np.unique(X)

    H_s = []
    w = []
    for c in classes:
        y_subset = y[X == c]
        w.append(len(y_subset) / len(X))
        H_s.append(calculate_entropy(y_subset))

    ig = parent_entropy - np.sum(np.array(w) * np.array(H_s))
    return float(ig)


def majority_class(examples: list[dict], target_attr: str) -> str:
    """Return the majority class. Break ties alphabetically."""
    # Your code here
    if not examples:
        return ""
    y_l = []
    for i in range(len(examples)):
        y_l.append(examples[i][target_attr])
    y = np.array(y_l)
    classes , count = np.unique(y, return_counts = True)
    return classes[np.argmax(count)]

def learn_decision_tree(examples: list[dict], attributes: list[str], target_attr: str) -> dict | str:
    """
    Build a decision tree using the ID3 algorithm with recursive splitting.
    """
    ## Edge case - empty dataset
    if not examples:
        return ""

    # Extract all target class labels present in the current subset
    labels = [ex[target_attr] for ex in examples]

    # Base Case 1: Pure Node
    # If all examples have the exact same target label (Entropy = 0),
    # stop recursion and return that label as a leaf node.
    if len(set(labels)) == 1:
        return labels[0]

    # Base Case 2: No Remaining Attributes
    # If there are no candidate attributes left to split on, but the node is
    # still impure, return the majority class label (with alphabetical tie-break).
    if not attributes:
        return majority_class(examples, target_attr)

    # Step 1: Attribute Selection via Information Gain
    best_attr = None
    max_ig = -float("inf")
    for attr in attributes:
        ig = calculate_information_gain(examples, attr, target_attr)
        if ig > max_ig:
            max_ig = ig
            best_attr = attr

    # Step 2: Initialize Decision Node & Attribute List for Children
    tree = {best_attr: {}}

    # The chosen splitting attribute must be removed from subsequent child splits
    remaining_attributes = [a for a in attributes if a != best_attr]

    # Collect and sort all distinct values of `best_attr` in this subset.
    unique_values = sorted(list({ex[best_attr] for ex in examples}))

    # Step 3: Recursive Branch Construction
    for val in unique_values:
        # Filter examples belonging to the current branch
        subset = [ex for ex in examples if ex[best_attr] == val]

        # Recurse on the partitioned subset with the reduced attribute list
        tree[best_attr][val] = learn_decision_tree(
            examples=subset,
            attributes=remaining_attributes,
            target_attr=target_attr
        )

    return tree