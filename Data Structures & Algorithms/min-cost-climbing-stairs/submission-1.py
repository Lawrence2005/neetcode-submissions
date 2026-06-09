class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        nextF, nextnextF = cost[-2], cost[-1]
        for i in range(len(cost) - 3, -1, -1):
            tmp = nextF
            nextF = cost[i] + min(nextF, nextnextF)
            nextnextF = tmp
        
        return min(nextF, nextnextF)