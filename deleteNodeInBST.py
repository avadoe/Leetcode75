def deleteNode(self, root, key):
    if not root: return None
    
    if key < root.val:
        root.left = self.deleteNode(root.left, key)
    elif key > root.val:
        root.right = self.deleteNode(root.right, key)
    else:
        if not root.left :
            return root.right
        elif not root.right:
            return root.left
        
        # To find inorder successor 
        
        currNode = root.right
        while currNode.left:
            currNode = currNode.left
            
        root.val = currNode.val
        root.right = self.deleteNode(root.right, currNode.val)
    return root
