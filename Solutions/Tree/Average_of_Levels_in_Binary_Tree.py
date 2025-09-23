# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        queue = deque([root])
        result = []
        while queue:
            total = 0.0
            n =len(queue)
            for i in range(n):
                r = queue.popleft()
                total += r.val
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            result.append(total / n)
        return result
