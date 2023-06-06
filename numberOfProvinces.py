def findCircleNum(isConnected):
    visited = set()
    provinces = 0
    
    def dfs(city):
        visited.add(city)
        for present, connectedcity in enumerate(isConnected[city]):
            if connectedcity and present not in visited:
                dfs(present)
    
    for i in range(len(isConnected)):
        if i not in visited:
            dfs(i)
            provinces += 1
            
    return provinces