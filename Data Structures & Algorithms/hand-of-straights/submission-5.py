class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        numCount, minH = {}, []
        for i in range(len(hand)):
            if hand[i] not in numCount:
                numCount[hand[i]] = 0
                heapq.heappush(minH, hand[i])
            numCount[hand[i]] += 1
        
        while minH:
            currMin = heapq.heappop(minH)
            minCount = numCount[currMin]
            if minCount == 0:
                continue
                
            for i in range(groupSize):
                if currMin + i not in numCount or numCount[currMin + i] < minCount:
                    return False
            
                numCount[currMin + i] -= minCount

        return True