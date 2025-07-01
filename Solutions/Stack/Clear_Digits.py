class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for ch in s:
            if ch.isdigit() and stack:
                stack.pop()
            elif ch.isalpha():
                stack.append(ch)
        return "".join(stack)
