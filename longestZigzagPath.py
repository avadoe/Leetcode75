def helper(self, root, left, length):
    if not root: return length
    
    if left:
        length = max(length, self.helper(root.right, False, length + 1), self.helper(root.left, True, 0))
    else:
        length = max(length, self.helper(root.left, True, length + 1), self.helper(root.right, False, 0))
        
    return length

def longestZigzagPath(self, root):
    # root is optional, since the longest zigzag path needn't start at the root node 
    return max(self.helper(root.left, True, 0), self.helper(root.right, False, 0))