def count_consonants(s):
    """
    Function to count the number of consonants in the input string.
    
    Parameters:
    s (str): The input string to check for consonants.
    
    Returns:
    int: The count of consonants in the input string.
    """
    # Your code here
    count = 0
    s = s.lower()
    for i in s:
        if i not in ['a', 'e', 'i', 'o', 'u', ' ', ',', '!']:
            count += 1
    return count


count_consonants("Dallas Fort Worth")