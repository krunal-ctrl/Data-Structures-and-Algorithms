# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    denominations = [1, 3, 4]
    dp_result = [0] + [-1] * money
    for i in range(1, money + 1):
        for j in denominations:
            if i >= j:
                coins = dp_result[i - j] + 1
                if (coins < dp_result[i]) or (dp_result[i] == -1):
                    dp_result[i] = coins
    return dp_result[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
