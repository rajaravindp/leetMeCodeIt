def count_words(s):
    # Your code here
    count = 0
    s = s.split()
    for i in s: 
        count += 1
    return count

count_words("United States of America")        