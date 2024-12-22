from utils import read, write


def patterns(pattern: str, string: str) -> str:
    n, m = len(pattern), len(string)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    dp[0][0] = True

    for i in range(1, n + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]
        else:
            break

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[i - 1] == string[j - 1] or pattern[i - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[i - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return 'YES' if dp[n][m] else 'NO'


def main():
    write(end='')
    data = [line for line in read(type_convert=str)]
    pattern, string = data[0][0], data[1][0]
    write(patterns(pattern, string), to_end=True)


if __name__ == '__main__':
    main()
