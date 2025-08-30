# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        count = [0]
        def inOrder(root):
            if root:
                inOrder(root.left)
                count[0] += 1
                inOrder(root.right)
        inOrder(root)
        return count[0]
