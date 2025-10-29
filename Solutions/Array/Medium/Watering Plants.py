class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        steps = 0
        current_water = capacity
        n = len(plants)

        for i in range(n):
            if plants[i] <= current_water:
                steps += 1
                current_water -= plants[i]
            else:
                steps += (i - -1) * 2 - 1
                current_water = capacity
                current_water -= plants[i]
        return steps
