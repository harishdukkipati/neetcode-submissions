# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:     
        def is_sub(pinky, winky):
            if not winky and not pinky:
                return True
            if not winky or not pinky:
                return False
            if winky.val != pinky.val:
                return False
            
            return is_sub(pinky.left, winky.left) and is_sub(pinky.right, winky.right)
        
        def search(node):
            if not node:
                return False
            
            if is_sub(node, subRoot):
                return True 
            
            return search(node.left) or search(node.right)
        
        return search(root)
        
        