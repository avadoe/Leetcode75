from collections import deque

def nearestExit(maze, entrance):
    rows = len(maze)
    cols = len(maze[0])
    
    entrance_row, entrance_col = entrance
    
    for i in range(len(rows)):
        if maze[i][0] == '.': maze[i][0] = 'e'
        if maze[i][-1] == '.': maze[i][-1] = 'e'
        
    for j in range(len(rows[0])):
        if maze[0][j] == '.': maze[0][j] = 'e'
        if maze[-1][j] == '.': maze[-1][j] = 'e'
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False] * cols for _ in range(rows)]
    queue = deque()
    
    queue.append((0, entrance_row, entrance_col))
    visited[entrance_row][entrance_col] = True
    
    while queue:
        distance, curr_row, curr_col = queue.popleft()
        
        for direction in directions:
            new_row, new_col = curr_row + direction[0], curr_col + direction[1]
            
            if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col]:
                if maze[new_row][new_col] == 'e':
                    visited[new_row][new_col] = True
                    queue.append((distance + 1, new_row, new_col))
                    
                elif maze[new_row][new_col] == 'e':
                    return distance + 1