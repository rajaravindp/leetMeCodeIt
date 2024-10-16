def phoneNumWords(input, idx = 0, curr = "", result = None):
    k = [
        [], 
        [], 
        ["A", "B", "C"], 
        ["D", "E", "F"],
        ["G", "H", "I"],
        ["J", "K", "L"],
        ["M", "N", "O"],
        ["P", "Q", "R", "S"],
        ["T", "U", "V"],
        ["W", "X", "Y", "Z"]
    ]

    if result is None:
        result = []

    if idx == len(input):
        result.append(curr)
        return result
    
    currDig = int(input[idx])
    kWords = k[currDig]

    for i in kWords:
        phoneNumWords(input, idx+1, curr + i, result)
    
    return result

print(phoneNumWords('23'))


# Time Complexity for both algorithms is O(3**n, 4**m)
# where n: # digits maping to 3 char
# where m: # digits maping to 4 char


# Method 2
def phoneNumWords1(input):
    k = {
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'Q', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y', 'Z']
    }
    if not input:
        return []
    if len(input) == 1:
        return k[input[0]]
    
    curr = k[input[0]]
    diff = phoneNumWords1(input[1:])

    arr = list()
    for i in curr:
        for j in diff:
            arr.append(i+j)
    return arr
print(phoneNumWords1('236'))