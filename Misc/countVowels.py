def count_vowels(s):
    """
    Function to count the number of vowels in the input string.
    
    Parameters:
    s (str): The input string to check for vowels.
    
    Returns:
    int: The count of vowels in the input string.
    """
    if not s:
        return None
    s = s.lower()
    res = 0
    for i in s: 
        if i in ["a", "e", "i", "o", "u"]:
            res += 1
    return res

count_vowels("India")
