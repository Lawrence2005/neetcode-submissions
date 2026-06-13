class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = []
        currGas, least = 0, (float('inf'), None)
        for i in range(len(gas)):
            currGas += gas[i] - cost[i]
            if currGas < least[0]:
                least = (currGas, i)
            tank.append(currGas)
        
        if tank[-1] < 0:
            return -1
        
        return (least[1] + 1) % len(gas)