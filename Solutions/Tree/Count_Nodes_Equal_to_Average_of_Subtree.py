# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        total = 0
        def inOrder(root):
            nonlocal total
            if root:
                if self.avg_subtree(root):
                    total += 1
                inOrder(root.left)
                inOrder(root.right)
        inOrder(root)
        return total

    def avg_subtree(self, root):
        total = 0
        ct = 0
        def inOrder(root):
            nonlocal ct
            nonlocal total
            if root:
                ct += 1
                total += root.val
                inOrder(root.left)
                inOrder(root.right)
        inOrder(root)
        return total // ct == root.val
