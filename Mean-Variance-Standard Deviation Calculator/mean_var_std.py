import numpy as np

def calculate(list: np.ndarray):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    new_list = np.reshape(list, (3, 3))

    calculations = {
        'mean': [new_list.mean(axis=0).tolist(), new_list.mean(axis=1).tolist(), new_list.mean()],
        'variance': [new_list.var(axis=0).tolist(), new_list.var(axis=1).tolist(), new_list.var()],
        'standard deviation': [new_list.std(axis=0).tolist(), new_list.std(axis=1).tolist(), new_list.std()],
        'max': [new_list.max(axis=0).tolist(), new_list.max(axis=1).tolist(), new_list.max()],
        'min': [new_list.min(axis=0).tolist(), new_list.min(axis=1).tolist(), new_list.min()],
        'sum': [new_list.sum(axis=0).tolist(), new_list.sum(axis=1).tolist(), new_list.sum()],
    }


    return calculations