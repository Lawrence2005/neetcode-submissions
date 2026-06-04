class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = defaultdict(list)
        for s in strs:
            count = [0 for _ in range(26)]
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            track[tuple(count)].append(s)
        
        return list(track.values())