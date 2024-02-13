def firstPalindrome(words: list[str]) -> str:
    try:
        s = next(
            filter(
                lambda s: s is not None,
                map(lambda s: s if s == s[::-1] else None, words),
            )
        )

    except StopIteration:
        s = ""

    return s if s else ""


def main():
    print(f"{firstPalindrome(words = ['abc','car','ada','racecar','cool'])=}")
    print(f"{firstPalindrome(words = ['notapalindrome','racecar'])=}")
    print(f"{firstPalindrome(words = ['def','ghi'])=}")


if __name__ == "__main__":
    main()
