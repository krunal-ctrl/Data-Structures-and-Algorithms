# python3

import math
def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    if n == 1:
        return [1]
    #     remaining = n
    else:

        m = 2 * int(math.sqrt(n)) + 1
        for i in range(1, m):
            if n > 2 * i:
                summands.append(i)
                n -= i
        else:
            summands.append(n)

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
