def sum_to_n(n: int) -> int:
    return n * (n + 1) // 2


def missingNumber(nums: list[int]) -> int:
    # nums.sort()

    # for i in range(0, len(nums)):
    #     if nums[i] != i:
    #         return i

    # return len(nums)

    sum = 0
    for i in range(0, len(nums)):
        sum += nums[i]

    return sum_to_n(len(nums)) - sum


def main():
    print(f"{missingNumber(nums = [3,0,1])=}")
    print(f"{missingNumber(nums = [0,1])=}")
    print(f"{missingNumber(nums = [9,6,4,2,3,5,7,0,1])=}")


if __name__ == "__main__":
    main()
