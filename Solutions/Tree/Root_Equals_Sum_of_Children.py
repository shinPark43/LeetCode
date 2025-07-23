# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        result = []
        def inOrderTraverse(root):
            if root:
                inOrderTraverse(root.left)
                result.append(root.val)
                inOrderTraverse(root.right)
        inOrderTraverse(root)
        return result[1] == result[0] + result[2]
