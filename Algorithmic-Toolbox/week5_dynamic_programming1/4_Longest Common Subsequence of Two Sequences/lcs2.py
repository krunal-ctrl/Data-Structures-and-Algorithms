# python3


def lcs2(a, b):
    assert len(a) <= 100
    assert len(b) <= 100

    import numpy as np
    dp = np.zeros((len(a) + 1, len(b) + 1))  # keep a matrix of size len(a)+1 and len(b)+1 first row and first column has 0s only as there is no matching at all. we use it for next rows and columns

    for i, number1 in enumerate(a):  # enumerate for index and values of both arrays, note that I am starting from index 0 but adding it as dp[i+1]dp[j+1]
        for j, number2 in enumerate(b):
            if number1 == number2:  # if numbers match, common sequence length increases by 1
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:  # else just take the max of the square just above or just left
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    return int(dp[len(a)][len(b)])


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
