class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = {}
        minH = []
        for num in hand:
            if num not in count:
                count[num] = 0
                heapq.heappush(minH, num)
            count[num] += 1

        while minH:
            currMin = heapq.heappop(minH)
            if count[currMin] == 0:
                continue

            for i in range(1, groupSize):
                if currMin + i not in count or count[currMin + i] < count[currMin]:
                    return False
                
                count[currMin + i] -= count[currMin]
            count[currMin] = 0
        return True