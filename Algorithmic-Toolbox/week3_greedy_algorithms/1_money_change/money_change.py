# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    total_coin = 0
    total_coin += (money // 10)
    money %= 10
    total_coin += (money // 5)
    total_coin += money % 5
    return total_coin

if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
