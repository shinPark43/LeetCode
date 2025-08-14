"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        def search(root):
            if root:
                if root.children:
                    for i in range(len(root.children)):
                        search(root.children[i])
                result.append(root.val)
        search(root)
        return result
