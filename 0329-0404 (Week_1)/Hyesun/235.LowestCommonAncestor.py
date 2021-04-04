#235. Lowest Common Ancestor of a Binary Search Tree
#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # case1: if both p, q are less than root
        if root.val > p.val and root.val > q.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        # case1: if both p, q are greater than root
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else: 
            return root
    
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
