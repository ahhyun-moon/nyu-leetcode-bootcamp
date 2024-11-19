# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Thought Process:
        # Find the last element in the level using BFS
        if root is None:
            return []
        queue = deque([[root, 1]])
        result = []
        while queue:
            element, level = queue.popleft()
            # Append to answer if current is the only element in the level
            # Or the last element in the last level
            if not queue: result.append(element.val)
            # Append to answer if current is the last element in the level
            elif queue and level < queue[0][1]: result.append(element.val)
            # Append to queue for BFS
            if element.left: queue.append([element.left, level + 1])
            if element.right: queue.append([element.right, level + 1])
        return result
        
