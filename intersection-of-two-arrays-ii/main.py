class Solution:
    def intersect(
        self, nums1: list[int], nums2: list[int]
    ) -> list[int]:
        intersection = []
        i, j = 0, 0

        nums1.sort()
        nums2.sort()

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersection.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return intersection
