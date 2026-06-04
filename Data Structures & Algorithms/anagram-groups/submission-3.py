class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = {}
        for s in strs:
            count = [0 for _ in range(26)]
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) in track:
                track[tuple(count)].append(s)
            else:
                track[tuple(count)] = [s]
        
        return[track[group] for group in track]