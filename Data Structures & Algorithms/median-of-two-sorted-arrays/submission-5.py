class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) >= len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        
        l, r = 0, m
        median = None
        while l <= r:
            nums1Len = l + (r - l) // 2
            nums2Len = (m + n + 1) // 2 - nums1Len

            left1 = nums1[nums1Len - 1] if nums1Len > 0 else float('-inf')
            right1 = nums1[nums1Len] if nums1Len < m else float('inf')

            left2 = nums2[nums2Len - 1] if nums2Len > 0 else float('-inf')
            right2 = nums2[nums2Len] if nums2Len < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0:
                    median = float(max(left1, left2) + min(right1, right2)) / 2
                else:
                    median = max(left1, left2)
                break

            if left1 > right2:
                r = nums1Len - 1
            else:
                l = nums1Len + 1

        return median