def maxProfit(prices: list[int]) -> int:
    max_profit = 0
    buy = 0
    sell = 1

    while sell < len(prices):
        if prices[sell] > prices[buy]:
            max_profit = max(max_profit, prices[sell] - prices[buy])
        else:
            buy = sell

        sell += 1

    return max_profit


def main():
    print(f"{maxProfit(prices = [7,1,5,3,6,4])=}")
    print(f"{maxProfit(prices = [7,6,4,3,1])=}")


if __name__ == "__main__":
    main()
