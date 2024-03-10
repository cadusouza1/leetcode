from collections import defaultdict


class Solution:
    def intersection(
        self, nums: list[list[int]]
    ) -> list[int]:
        intersect = []
        frequencies = defaultdict(int)

        for arr in nums:
            for num in arr:
                frequencies[num] += 1

        for num, frequency in frequencies.items():
            if frequency == len(nums):
                intersect.append(num)

        return sorted(intersect)
