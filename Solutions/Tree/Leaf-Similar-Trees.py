# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        val_list = []
        def dfs(root):
            total = 0
            if root:
                if root.left:
                    dfs(root.left)
                else:
                    total += 1
                if root.right:
                    dfs(root.right)
                else:
                    total += 1
                if total == 2:
                    val_list.append(root.val)
        dfs(root1)
        root1_list = val_list
        val_list = []
        dfs(root2)
        return root1_list == val_list
