def lengthOfLastWord(s: str) -> int:
    size = 0

    for char in s.rstrip()[::-1]:
        if char == " ":
            return size

        size += 1

    return size


def main():
    print(f"{lengthOfLastWord(s='Hello World')=}")
    print(f"{lengthOfLastWord(s='   fly me   to   the moon  ')=}")
    print(f"{lengthOfLastWord(s='luffy is still joyboy')=}")
    print(f"{lengthOfLastWord(s = 'a')=}")


if __name__ == "__main__":
    main()
