class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.result = []
        self.helper(candidates, target, 0, [], 0)
        return self.result
    
    def helper(self, candidates, target, idx, subset, currSum):
        if currSum >= target or idx >= len(candidates):
            if currSum == target:
                self.result.append(subset[:])
            
            return
        
        subset.append(candidates[idx])
        self.helper(candidates, target, idx + 1, subset, currSum + candidates[idx])

        subset.pop()
        nextIdx = idx + 1
        while nextIdx < len(candidates) and candidates[nextIdx] == candidates[idx]:
            nextIdx += 1
        self.helper(candidates, target, nextIdx, subset, currSum)

        return