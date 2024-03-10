from functools import reduce
from typing import Counter


class Solution:
    def intersection(
        self, nums: list[list[int]]
    ) -> list[int]:
        frequencies = reduce(
            lambda acc, counter: acc + counter,
            map(lambda arr: Counter(arr), nums),
        )

        return sorted(
            filter(
                lambda k: frequencies[k] == len(nums),
                frequencies,
            )
        )
