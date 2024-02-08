def removeDuplicates(nums: list[int]) -> int:
    j = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1

    return j


def main():
    nums = [1, 1, 2]
    print(f"{removeDuplicates(nums)=}")
    print(f"{nums=}")

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(f"{removeDuplicates(nums)=}")
    print(f"{nums=}")


if __name__ == "__main__":
    main()
