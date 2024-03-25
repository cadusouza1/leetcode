class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        res = []

        for num in nums:
            num = abs(num)
            if nums[num - 1] < 0:
                res.append(num)

            nums[num - 1] *= -1

        return res


