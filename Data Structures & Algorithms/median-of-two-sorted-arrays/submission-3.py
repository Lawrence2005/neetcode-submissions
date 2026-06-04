class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)

        left, right = 0, m
        while left <= right:
            cut1 = left + (right - left) // 2
            cut2 = (m + n + 1) // 2 - cut1

            maxLeft1 = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
            minRight1 = nums1[cut1] if cut1 < m else float('inf')

            maxLeft2 = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
            minRight2 = nums2[cut2] if cut2 < n else float('inf')

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 0:
                    return float(max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                return max(maxLeft1, maxLeft2)

            if maxLeft1 > minRight2:
                right = cut1 - 1
            else:
                left = cut1 + 1
        
        return -1