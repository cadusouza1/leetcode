def twoSum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left + 1, right + 1]
        elif sum > target:
            right -= 1
        else:
            left += 1

    return [-1, -1]


def main():
    print(f"{twoSum(numbers = [2,7,11,15], target = 9)=}")
    print(f"{twoSum(numbers = [2,3,4], target = 6)=}")
    print(f"{twoSum(numbers = [-1,0], target = -1)=}")


if __name__ == "__main__":
    main()
