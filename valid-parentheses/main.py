def isValid(s: str) -> bool:
    stack = []
    closed_to_open_map = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for c in s:
        if c in closed_to_open_map:
            if stack and stack[-1] == closed_to_open_map[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return stack == []


def main():
    s = ["()", "()[]{}", "(]", "([)]", "{[]}"]

    for v in s:
        print(f"{isValid(v)=}")


if __name__ == "__main__":
    main()
