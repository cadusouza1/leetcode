def rearrangeArray(nums: list[int]) -> list[int]:
    positive = filter(lambda x: x >= 0, nums)
    negative = filter(lambda x: x < 0, nums)
    sorted_nums = []

    for p, n in zip(positive, negative):
        sorted_nums.append(p)
        sorted_nums.append(n)

    return sorted_nums


def main():
    print(f"{rearrangeArray(nums = [3,1,-2,-5,2,-4])=}")
    print(f"{rearrangeArray(nums = [-1,1])=}")


if __name__ == "__main__":
    main()
