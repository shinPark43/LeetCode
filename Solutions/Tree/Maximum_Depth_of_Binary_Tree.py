# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue = deque([root])
        depth = 0
        while queue:
            for i in range(len(queue)):
                r = queue.popleft()
                if not r:
                    return depth
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            depth += 1
        return depth
