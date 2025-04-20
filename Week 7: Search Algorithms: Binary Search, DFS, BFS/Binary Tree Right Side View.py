# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = {}
        queue = deque([(root,0)])

        while queue:
            node, depth = queue.popleft()
            if node:
                ret[depth] = node.val
                queue.append((node.left, depth+1))
                queue.append((node.right, depth+1))
        
        return list(ret.values())