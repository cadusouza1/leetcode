from typing import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freqs = Counter(nums)

        for num, freq in freqs.items():
            if freq > len(nums) // 2:
                return num

        return -1
