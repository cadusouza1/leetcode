from collections import defaultdict
from typing import Counter


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        num_to_frequencies = Counter(nums)
        frequencies_to_nums = defaultdict(int)

        for count in num_to_frequencies.values():
            frequencies_to_nums[count] += 1

        key_max_frequency = max(frequencies_to_nums.keys())

        return (
            key_max_frequency
            * frequencies_to_nums[key_max_frequency]
        )
