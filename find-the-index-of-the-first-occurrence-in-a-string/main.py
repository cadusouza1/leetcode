def strStr(haystack: str, needle: str) -> int:
    i = 0

    while i < len(haystack):
        if haystack[i : i + len(needle)] == needle:
            return i

        i += 1

    return -1


def main():
    print(f"{strStr(haystack = 'sadbutsad', needle = 'sad')=}")
    print(f"{strStr(haystack = 'leetcode', needle = 'leeto')=}")
    print(f"{strStr(haystack = 'mississippi', needle = 'issi')=}")


if __name__ == "__main__":
    main()
