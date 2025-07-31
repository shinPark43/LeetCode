# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        queue_p = deque([p])
        queue_q = deque([q])

        while queue_p and queue_q:
            r = queue_p.popleft()
            t = queue_q.popleft()
            
            if not r and not t:
                continue
            elif not r or not t:
                return False
            elif r.val != t.val:
                return False

            queue_p.append(r.left)
            queue_q.append(t.left)
            queue_p.append(r.right)
            queue_q.append(t.right)
        return queue_p == queue_q
