class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        time = []
        for car in cars:
            time.append((target - car[0]) / car[1])
        
        stack = []
        for t in time:
            if not stack or stack[-1] < t:
                stack.append(t)
            
        return len(stack)