class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count, minH = {}, []
        for i in range(len(hand)):
            if hand[i] not in count:
                count[hand[i]] = 0
                heapq.heappush(minH, hand[i])
            count[hand[i]] += 1
        
        while minH:
            currMin = heapq.heappop(minH)
            if count[currMin] == 0:
                continue
            
            freq = count[currMin]
            for i in range(groupSize):
                if count.get(currMin + i, 0) < freq:
                    return False
                
                count[currMin + i] -= freq
        return True