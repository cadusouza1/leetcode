def plusOne(digits: list[int]) -> list[int]:
    sum = digits[-1] + 1
    digits[-1] = sum % 10
    carry = sum // 10

    for i in range(len(digits) - 2, -1, -1):
        if carry == 0:
            return digits

        sum = digits[i] + carry
        digits[i] = sum % 10
        carry = sum // 10

    if carry != 0:
        digits.insert(0, carry)

    return digits


def main():
    print(f"{plusOne(digits=[1,2,3])=}")
    print(f"{plusOne(digits=[4,3,2,1])=}")
    print(f"{plusOne(digits=[9])=}")
    print(f"{plusOne(digits=[9, 9])=}")
    print(f"{plusOne(digits=[9, 9, 9])=}")


if __name__ == "__main__":
    main()
