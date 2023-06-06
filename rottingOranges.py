from collections import deque

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    
    queue = deque()
    count = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1: count +=1 
            elif grid[i][j] == 2: queue.append((i, j))
            
    res = 0
    
    while queue:
        for _ in range(len(queue)):
            i, j = queue.popleft()
            
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                    grid[x][y] = 2
                    count -= 1
                    queue.append((x, y))

        res += 1
        
    return max(res - 1, 0) if count == 0 else -1
