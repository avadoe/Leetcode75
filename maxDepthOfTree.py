def maxDepth(root):
    def dfs(root, depth):
        if not root: return 0
        return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
    return dfs(root, 0)