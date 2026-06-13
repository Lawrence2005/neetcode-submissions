class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        maxTrips = [float('-inf'), float('-inf'), float('-inf')]
        for i in range(len(triplets)):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                continue

            maxTrips = [max(maxTrips[0], triplets[i][0]), max(maxTrips[1], triplets[i][1]), max(maxTrips[2], triplets[i][2])]
        return maxTrips == target