class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        mini = (float('inf'), 0)
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < mini[0]:
                mini = (total, i)
        if total < 0:
            return -1
        
        return (mini[1] + 1) % len(gas)