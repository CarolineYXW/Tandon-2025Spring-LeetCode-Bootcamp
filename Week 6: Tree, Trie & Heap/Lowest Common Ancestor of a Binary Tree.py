# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root.val == p.val or root.val == q.val:
            return root
        right = self.lowestCommonAncestor(root.right, p, q)
        left = self.lowestCommonAncestor(root.left, p, q)
        if not left and not right:
            return 0
        elif not left:
            return right
        elif not right:
            return left
        else:
            return root