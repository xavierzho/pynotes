"""
@Author: Jonescyna@gmail.com
@Created: 2020/12/23
"""


def lcs_length(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # 定义1为左上方2为上方3为左
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:  # i, j上的字符匹配的时候，来自于左上+1
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1   # 1
            elif c[i - 1][j] > c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = 2  # 2
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 3  # 3
    return c[m][n], b


def lcs_traceback(x, y):
    c, b = lcs_length(x, y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        if b[i][j] == 1:  # 来自左上方=》匹配
            res.append(x[i - 1])
            i -= 1
            j -= 1
        elif b[i][j] == 2:  # 来自上方
            i -= 1
        else:  # 来自左方
            j -= 1
    return ''.join(reversed(res))


b = lcs_traceback('ABCBDAB', 'BDCABA')
print(b)

