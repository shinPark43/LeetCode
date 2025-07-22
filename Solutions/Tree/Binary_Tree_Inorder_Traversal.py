# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    result = []
    def traverse(self, root):
        if root:

            self.traverse(root.left)
            self.result.append(root.val)
            self.traverse(root.right)

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if self.result:
            self.result = []

        self.traverse(root)
        return self.result
