# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        def explore(curr: TreeNode) -> bool:
            if not curr: # If None (end of branch) return False
                return False
            left = explore(curr.left)
            right = explore(curr.right)
            mid = (curr == p) or (curr == q)
            if mid + left + right >= 2: # Return curr if two or more conditions are True
                self.ans = curr 
            return mid or left or right # Check for any True condition

        explore(root)
        return self.ans
            
            