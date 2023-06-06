import collections

def calcEquation(equations, values, queries):
    adj = collections.defaultdict(list)
    
    for i, eq in enumerate(equations):
        a, b = eq
        adj[a].append([b, values[i]])
        adj[b].append([a, 1 / values[i]])
        
    def bfs(src, target):
        if src not in adj or target not in adj:
            return -1
        
        q, visit = collections.deque(), set()
        
        q.append([src, 1])
        
        while q:
            n, w = q.popleft()
            if n == target: return w
            
            for neighbor, weight in adj[n]:
                if neighbor not in visit:
                    q.append([neighbor, weight * w])
                    visit.add(neighbor)
                
        return -1
        
    return [bfs(q[0], q[1]) for q in queries]
    