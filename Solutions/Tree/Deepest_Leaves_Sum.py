# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue = deque()
        queue.append(root)
        stack = []
        total = 0

        while queue:
            n = len(queue)
            for i in range(n):
                r = queue.popleft()
                stack.append(r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            if not queue:
                for i in range(n):
                    total += stack.pop()
        return total
