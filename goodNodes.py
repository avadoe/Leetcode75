def goodNodes(root):
    def helper(node, prev):
        if not node: return 0
        res = 1 if node.val >= prev else 0
        res += helper(node.left, max(prev, node.val))
        res += helper(node.right, max(prev, node.val))
        
        return res
    return helper(root, -10000)