from collections import deque

def rightView(root):
    if not root: return []
    ans = []
    
    queue = deque([root])
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.popleft()
            if i == 0:
                ans.push(node.val)
            
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
                
    return ans

            
    