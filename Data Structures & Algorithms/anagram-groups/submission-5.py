class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = {}
        for s in strs:
            letters = [0 for _ in range(26)]
            for c in s:
                letters[ord(c) - ord('a')] += 1
            
            if tuple(letters) in track:
                track[tuple(letters)].append(s)
            else:
                track[tuple(letters)] = [s]
        
        return list(track.values())