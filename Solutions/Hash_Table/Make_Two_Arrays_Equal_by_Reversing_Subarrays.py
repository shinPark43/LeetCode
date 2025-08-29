class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        target_dict = {}
        for num in target:
            if num not in target_dict:
                target_dict[num] = 1
            else:
                target_dict[num] += 1
        arr_dict = {}
        for num in arr:
            if num not in arr_dict:
                arr_dict[num] = 1
            else:
                arr_dict[num] += 1

        arr_set = set(arr)

        for num,val in target_dict.items():
            if num not in arr_set:
                return False
            elif val != arr_dict[num]:
                return False
                
        return True
