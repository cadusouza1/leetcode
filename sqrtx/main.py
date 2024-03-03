def mySqrt(x: int) -> int:
    for i in range(0, x + 1):
        print(i * i)
        if i * i == x:
            return i

        if i * i > x:
            return i - 1

    return -1

