# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# from collections import deque
class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        # queue = deque()
        # queue.append(cloned)
        
        # while queue:

        #     r = queue.popleft()

        #     if r.val == target.val:
        #         return r
        #     if r.left:
        #         queue.append(r.left)
        #     if r.right:
        #         queue.append(r.right)
        # return None
        def dfs(root):
            if not root:
                return None
            if root.val == target.val:
                return root
            return dfs(root.left) or dfs(root.right)
        return dfs(cloned)
