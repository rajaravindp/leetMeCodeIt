def is_anagram(s, t):
    """
    Function to check if t is an anagram of s.
    
    Parameters:
    s (str): The first input string.
    t (str): The second input string.
    
    Returns:
    bool: True if t is an anagram of s, False otherwise.
    """
    # Your code here
    if len(s) != len(t):
        return False
    for i in s:
        if i not in t:
            return False
    return True

s = "anagram"
t = "nagaram"
is_anagram(s, t)