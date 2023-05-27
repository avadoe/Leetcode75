def lowestCommonAncestor(root, node1, node2):
    def findPath(node, target, path):
        if not node: return False
        path.append(node.val)
        if node.val == target: return True
        
        if findPath(node.left, target, path) or findPath(node.right, target, path):
            return True
        
        path = path[:len(path) - 1]
        return False
    
    p1 = []
    p2 = []
    
    if not findPath(root, node1.val, p1) or not findPath(root, node2.val, p2):
        return -1
    
    temp = 0
    while temp < len(p1) and temp < len(p2) and p1[temp] == p2[temp]:
        temp += 1
        
    return p1[temp - 1]