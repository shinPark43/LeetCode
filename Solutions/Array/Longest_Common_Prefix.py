class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_length = 200
        prefix = ""
        for i in range(len(strs)):
            if len(strs[i]) < min_length:
                min_length = len(strs[i])
        for i in range(min_length):
            char = strs[0][i]
            is_prefix = True
            for j in range(1, len(strs)):
                if char != strs[j][i]:
                    is_prefix = False
                    break
            if is_prefix:
                prefix += char
            else:
                return prefix
        return prefix
