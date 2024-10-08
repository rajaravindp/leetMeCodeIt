def is_subset(lst1, lst2):
    for i in lst1:
        if i not in lst2:
            return False
    return True
    pass

# lst1 = [1, 2, 3]
lst1 = [1, 6]
# lst2 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3, 4, 5]
is_subset(lst1, lst2)