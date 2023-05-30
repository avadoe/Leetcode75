def equalPairs(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    columns = [[] for _ in range(cols)]
    
    for j in range(cols):
        for i in range(rows):
            columns[j].append(grid[i][j])
            
    ans = 0        
    
    for column in columns:
        for row in grid:
            ans += (column == row)
            
    return ans

grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
print(equalPairs(grid))