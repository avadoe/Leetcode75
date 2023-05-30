def pathSum(root, targetSum):
    if not root: return 0
    
    def dfs(root, targetSum):
        if not root: return 0
        
        return root.val == targetSum + dfs(root.left, targetSum - root.val) + dfs(root.right, targetSum - root.va)
    
    return dfs(root, targetSum) + pathSum(root.left, targetSum - root.val) + pathSum(root.right, targetSum - root.val)