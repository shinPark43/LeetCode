# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        val_list = []
        def inOrder(root):
            if root:
                inOrder(root.left)
                val_list.append(root.val)
                inOrder(root.right)
        inOrder(root)
        left_branch_list = []
        def rootAndRightSubtree(root):
            if root:
                rootAndRightSubtree(root.left)
                temp = root.val
                root.val = sum(val_list) - sum(left_branch_list)
                left_branch_list.append(temp)
                rootAndRightSubtree(root.right)
        rootAndRightSubtree(root)
        return root
