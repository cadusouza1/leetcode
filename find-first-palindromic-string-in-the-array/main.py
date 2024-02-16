def firstPalindrome(words: list[str]) -> str:
    try:
        return next(filter(lambda s: s == s[::-1], words))
    except StopIteration:
        return ""


def main():
    print(f"{firstPalindrome(words = ['abc','car','ada','racecar','cool'])=}")
    print(f"{firstPalindrome(words = ['notapalindrome','racecar'])=}")
    print(f"{firstPalindrome(words = ['def','ghi'])=}")


if __name__ == "__main__":
    main()
