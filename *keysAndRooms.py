# rooms[i] is the set of keys that you can obtain if you visited room i, 
# return true if you can visit all the rooms, or false otherwi

def canVisitAllRooms(rooms):
    total_rooms = len(rooms)
    visited = set()
    
    def dfs(room):
        visited.add(room)
        
        for key in rooms[room]:
            if key not in visited:
                dfs(key)
                
    dfs(0)
    
    return len(visited) == total_rooms

print(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))