class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        result = ""
        times_and_vals = self.map[key]
        left, right = 0, len(times_and_vals) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if times_and_vals[mid][0] == timestamp:
                return times_and_vals[mid][1]
            
            if times_and_vals[mid][0] < timestamp:
                result = times_and_vals[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return result
