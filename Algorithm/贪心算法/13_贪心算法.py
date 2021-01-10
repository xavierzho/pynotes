# 找零问题

t = [100, 50, 20, 5, 1]  # 钱的面值


def change(n):
    # 376
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money
        n = n % money
    return m, n


# print(change(376))


# 背包问题
goods = [(60, 10), (100, 20), (120, 30)]


def fractional_backpack(w):
    goods.sort(key=lambda x: x[0] / x[1], reverse=True)
    m = [0 for _ in range(len(goods))]
    total_v = 0
    for i, (price, weight) in enumerate(goods):
        if w >= weight:

            m[i] = 1
            total_v += price
            w -= weight
        else:
            m[i] = w / weight
            total_v += m[i] * price
            w = 0
            break
    return total_v, m


print(fractional_backpack(50))
