class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        least = (float('inf'), None)
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < least[0]:
                least = (total, i)
        
        if total < 0:
            return -1
        
        return (least[1] + 1) % len(gas)