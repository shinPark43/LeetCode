class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        hash_map = {}
        list_one = s1.split(' ')
        list_two = s2.split(' ')
        combined_list = list_one + list_two

        for word in combined_list:
            if word not in hash_map:
                hash_map[word] = 1
            else:
                hash_map[word] += 1
        result = []
        for word, count in hash_map.items():
            if count == 1:
                result.append(word)
        return result
    
