def merge_three_dictionaries(dict1, dict2, dict3):
    dict1.update(dict2)
    dict1.update(dict3)
    return dict1
    pass

merge_three_dictionaries({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})