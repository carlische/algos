from utils import write, read


def primitive_calculator(n):
    dp = [float('inf')] * (n + 1)
    prev = [-1] * (n + 1)

    dp[1] = 0

    for i in range(1, n + 1):
        if i + 1 <= n:
            if dp[i + 1] > dp[i] + 1:
                dp[i + 1] = dp[i] + 1
                prev[i + 1] = i

        if i * 2 <= n:
            if dp[i * 2] > dp[i] + 1:
                dp[i * 2] = dp[i] + 1
                prev[i * 2] = i

        if i * 3 <= n:
            if dp[i * 3] > dp[i] + 1:
                dp[i * 3] = dp[i] + 1
                prev[i * 3] = i

    path = []
    current = n
    while current != 1:
        path.append(current)
        current = prev[current]
    path.append(1)
    path.reverse()

    return [dp[n]], path


def main():
    write(end='')
    n, = read(type_convert=int)
    n = n[0]
    result = primitive_calculator(n)
    for line in result:
        write(*line, to_end=True)


if __name__ == '__main__':
    main()
