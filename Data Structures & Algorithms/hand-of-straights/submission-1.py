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

            freq = count[currMin]
            for i in range(groupSize):
                if count.get(currMin + i, 0) < freq:
                    return False
                
                count[currMin + i] -= freq

        return True