# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        q = []
        current_level = 0
        q.append(root)

        odd_tree_values = []

        while q:
            for i in range(len(q)):
                r = q.pop(0)

                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
                if current_level % 2 != 0:
                    r.val = odd_tree_values.pop()
                elif r.left and r.right and current_level % 2 == 0:
                    odd_tree_values.append(r.left.val)
                    odd_tree_values.append(r.right.val)
            current_level += 1
        return root
