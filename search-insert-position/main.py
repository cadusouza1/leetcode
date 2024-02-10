def binary_search(nums: list[int], target: int, low: int, high: int) -> int:
    if low == high:
        return low

    middle = (low + high) // 2

    if nums[middle] == target:
        return middle
    elif nums[middle] < target:
        return binary_search(nums, target, middle + 1, high)
    else:
        return binary_search(nums, target, low, middle)


def searchInsert(nums: list[int], target: int) -> int:
    return binary_search(nums, target, 0, len(nums))


def main():
    print(f"{searchInsert(nums=[1,3,5,6], target=5) = }")
    print(f"{searchInsert(nums=[1,3,5,6], target=2) = }")
    print(f"{searchInsert(nums=[1,3,5,6], target=7) = }")
    print(f"{searchInsert(nums=[1,3], target=2) = }")


if __name__ == "__main__":
    main()
