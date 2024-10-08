from collections import defaultdict

def merge_lists_to_dictionary(keys, values):
    if len(keys) != len(values):
        return None
    res = {}
    for i, j in zip(keys, values):
        res[i] = j
    return res

keys = ['a', 'b', 'c']
values = [1, 2, 3]
merge_lists_to_dictionary(keys, values)