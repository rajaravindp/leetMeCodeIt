def countNegatives(grid):
    # Implement your solution here
    cnt = 0
    for i in grid:
        for j in range(0, len(i)):
            if i[j] < 0:
                cnt += 1
    return cnt
    pass

grid = [[3, 2], [1, 0]] 
# grid = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
print(countNegatives(grid))