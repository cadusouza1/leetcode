from collections import defaultdict


def findJudge(n: int, trust: list[list[int]]) -> int:
    if n == 1:
        return 1

    incoming = defaultdict(int)
    outgoing = defaultdict(int)

    for a, b in trust:
        outgoing[a] += 1
        incoming[b] += 1

    for k, v in incoming.items():
        if v == n - 1 and outgoing[k] == 0:
            return k

    return -1


def main() -> None:
    print(f"{findJudge(n = 2, trust = [[1,2]])=}")
    print(f"{findJudge(n = 3, trust = [[1,3],[2,3]])=}")
    print(f"{findJudge(n = 3, trust = [[1,3],[2,3],[3,1]])=}")
    print(f"{findJudge(n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]])=}")


if __name__ == "__main__":
    main()
