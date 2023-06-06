def minReorder(n, connections):
    edges = {(a, b) for a, b in connections}
    neighbors = {city : [] for city in range(n)}
    visited = set()
    count = 0
    
    for a, b in connections:
        neighbors[a].append(b)
        neighbors[b].append(a)
        
    def dfs(city):
        nonlocal edges, neighbors, visited, count
        
        for neighbor in neighbors[city]:
            if neighbor in visited:
                continue
            
            if (neighbor, city) not in edges:
                count += 1
                
            visited.add(neighbor)
            dfs(neighbor)
            
    visited.add(0)
    dfs(0)
    
    return count