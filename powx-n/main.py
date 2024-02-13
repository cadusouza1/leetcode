import time


def myPow(x: float, n: int) -> float:
    def _pow(x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = _pow(x * x, n // 2)
        return x * res if n % 2 == 1 else res

    res = _pow(x, abs(n))
    return res if n >= 0 else 1 / res


def main():
    print(f"{myPow(x = 2.00000, n = 10)=}")
    print(f"{myPow(x = 2.10000, n = 3)=}")
    print(f"{myPow(x = 2.00000, n = -2)=}")


if __name__ == "__main__":
    main()
