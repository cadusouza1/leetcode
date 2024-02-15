def largestPerimeter(nums: list[int]) -> int:
    perimeter = 0
    max_perimeter = -1

    nums.sort()

    for side in nums:
        if perimeter > side:
            max_perimeter = perimeter + side

        perimeter += side

    return max_perimeter


def main():
    print(f"{largestPerimeter(nums = [5,5,5])=}")
    print(f"{largestPerimeter(nums = [1,12,1,2,5,50,3])=}")
    print(f"{largestPerimeter(nums = [5,5,50])=}")


if __name__ == "__main__":
    main()
