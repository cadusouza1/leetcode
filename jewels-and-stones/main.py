from typing import Counter


class Solution:
    def numJewelsInStones(
        self, jewels: str, stones: str
    ) -> int:
        freqs = Counter(stones)

        return sum(map(lambda jewel: freqs[jewel], jewels))
