# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        swap = curr.left
        curr.left = curr.right
        curr.right = swap

        self.invertTree(curr.left)
        self.invertTree(curr.right)
    
        
            



    

        
        