def leafSimilarTrees(root1, root2):
    def dfs(node):
        l = []
        if node: 
            if not node.left and not node.right: l.append(node.val)
            l += dfs(node.left)
            l += dfs(node.right)
        return l
    
    l1 = dfs(root1)
    l2 = dfs(root2)
    return l1 == l2