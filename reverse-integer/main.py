def reverse(x: int) -> int:
    digits = []
    num = 0
    sign = 1

    if x < 0:
        sign = -1
        x *= sign

    while x != 0:
        digits.append(x % 10)
        x = x // 10

    digits.reverse()
    for exponent, digit in enumerate(digits):
        num += digit * 10**exponent

    if num > 2**31 - 1:
        return 0

    return num * sign


def main():
    print(f"{reverse(x= 123)=}")
    print(f"{reverse(x=-123)=}")
    print(f"{reverse(x= 120)=}")
    print(f"{reverse(x= 1534236469)=}")


if __name__ == "__main__":
    main()
