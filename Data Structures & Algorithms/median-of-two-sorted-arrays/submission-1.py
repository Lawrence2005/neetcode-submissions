class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        minLen = min(len(nums1), len(nums2))
        search_list = nums1 if minLen == len(nums1) else nums2
        other_list = nums2 if minLen == len(nums1) else nums1

        result = None
        left, right = 0, minLen
        while left <= right:
            mid = left + (right - left) // 2
            maxLeft_search = search_list[mid - 1] if mid > 0 else -float('inf')
            minRight_search = search_list[mid] if mid < minLen else float('inf')

            other_list_cut = (len(nums1) + len(nums2) + 1) // 2 - mid
            maxLeft_other = other_list[other_list_cut - 1] if other_list_cut > 0 else -float('inf')
            minRight_other = other_list[other_list_cut] if other_list_cut < len(other_list) else float('inf')

            if maxLeft_search > minRight_other:
                right = mid - 1
            elif minRight_search < maxLeft_other:
                left = mid + 1
            else:
                if (len(nums1) + len(nums2)) % 2 != 0:
                    result = max(maxLeft_search, maxLeft_other)
                else:
                    result = float(max(maxLeft_search, maxLeft_other) + min(minRight_search, minRight_other)) / 2
                break

        return result