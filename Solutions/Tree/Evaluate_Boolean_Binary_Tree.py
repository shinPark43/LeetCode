# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(root):
            if root:
                if root.left == None and root.right == None:
                    return root.val
                if root.val == 2:
                    return dfs(root.left) or dfs(root.right)
                else:
                    return dfs(root.left) and dfs(root.right)
            else:
                return None
        return dfs(root) == 1
