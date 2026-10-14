import pandas as pd
def balance_undersample(data: list) -> list:
    """
    Undersample the majority classes so all classes have the same number of
    samples equal to the minority class count.

    data: list of (sample, label) tuples
    Returns: list of (sample, label) tuples, order-preserving
    """
    if data == []:
        return []

    df = pd.DataFrame(data)
    cat = df[1].value_counts()
    minimum = min(cat)
    
    lis = [] 
    
    for label in cat.index:
        x = df[df[1] == label][:minimum]
        lis.append(x)
        
    listt = pd.concat(lis).sort_index()
    
    return [tuple(r) for r in listt.values]