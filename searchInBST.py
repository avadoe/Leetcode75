def search(self, root, target):
    if not root: return None
    
    if root.val == target:
        return root
    elif target > root.val:
        return self.search(root.right, target)
    else:
        return self.search(root.left, target)
    