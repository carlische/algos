from utils import read, write


def coin_exchange(money, coins):
    dp = [float('inf')] * (money + 1)

    dp[0] = 0

    for i in range(1, money + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[money]


def main():
    write(end='')
    data = [list(line) for line in read(type_convert=int)]
    money, k = data[0]
    coins = data[1]
    write(coin_exchange(money, coins), to_end=True)


if __name__ == '__main__':
    main()
