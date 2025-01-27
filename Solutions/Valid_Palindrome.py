class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = ""
        for i in s:
            if i.isalnum():
                temp += i.lower()
        rev_temp = list(temp)
        rev_temp.reverse()
        if "".join(rev_temp) == temp:
            return True
        return False