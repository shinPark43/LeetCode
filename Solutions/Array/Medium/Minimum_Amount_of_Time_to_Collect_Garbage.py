class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        fardest_for_M = -1
        fardest_for_P = -1
        fardest_for_G = -1
        total_time = 0

        for i in range(len(garbage)):
            if 'M' in garbage[i]:
                fardest_for_M = i
            if 'P' in garbage[i]:
                fardest_for_P = i
            if 'G' in garbage[i]:
                fardest_for_G = i

        # Metal truck
        if fardest_for_M > -1:
            for i in range(fardest_for_M + 1):
                if 'M' in garbage[i]:
                    total_time += garbage[i].count('M')
                if i > 0:
                    total_time += travel[i - 1]

        # Paper truck
        if fardest_for_P > -1:
            for i in range(fardest_for_P + 1):
                if 'P' in garbage[i]:
                    total_time += garbage[i].count('P')
                if i > 0:
                    total_time += travel[i - 1]

        # Glass truck
        if fardest_for_G > -1:
            for i in range(fardest_for_G + 1):
                if 'G' in garbage[i]:
                    total_time += garbage[i].count('G')
                if i > 0:
                    total_time += travel[i - 1]
        return total_time