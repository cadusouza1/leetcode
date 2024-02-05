# O(N^2) Solution
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


def main():
    print(
        f"""
O(N^2) Solution:
Input: nums = [2,7,11,15], target = 9
Output: {twoSum(nums = [2,7,11,15], target = 9)}

Input: nums = [3,2,4], target = 6
Output: {twoSum( nums = [3,2,4], target = 6)}

Input: nums = [3,3], target = 6
Output: {twoSum( nums = [3,3], target = 6)}
        """
    )


if __name__ == "__main__":
    main()
