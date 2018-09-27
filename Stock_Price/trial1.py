# Enter your code here. Read input from STDIN. Print output to STDOUT
# Q: stock trading. Given daily stock prices of Z.
# prices: int[], prices[i] price of Z on day i
# Goal: write a fun. that computes maximum profit you can make
# by trading at most once (buy and sell 1 share once. Sell must happen after buy)

# Follow up: what if you can trade at most twice (buy 1st  sell 1st, buy 2nd, sell 2nd)


def max_profit(a):
    profit = 0
    if a is None or len(a) <= 1:
        return profit

    min_so_far = a[0]

    for i in range(1, len(a)):
        potential_profit = a[i] - min_so_far
        if potential_profit > profit:
            profit = potential_profit

        if a[i] < min_so_far:
            min_so_far = a[i]

    return profit


print(max_profit([1, 1, 1]))
print("---------")

print(max_profit([2, 5, 3, 6, 8, 1]))
print("---------")

print(max_profit([2, 5, 7, 100, 2, 8, 9]))
print("---------")


# trade1 ->   [0, i]  -> mp_i
# trade2 ->   [j, len(n) - 1] -> mp_j(given # i < j, max(price[i] - price[j]))
# return max((mp_i + mp_j), max_profit(a))

def find_i_j(a):
    loss = 0
    _i = _j = 0

    # # O(n^2)
    # for i in range(len(a)):
    #     for j in range(i + 1, len(a)):
    #         _l = a[i] - a[j]
    #         if _l > loss:
    #             loss = _l
    #             _i = i
    #             _j = j

    # O(n)
    idx_max_so_far = 0
    for k in range(1, len(a)):
        potential_loss = a[idx_max_so_far] - a[k]
        if potential_loss > loss:
            loss = potential_loss
            _i = idx_max_so_far
            _j = k

        if a[k] > a[idx_max_so_far]:
            idx_max_so_far = k

    return _i, _j


def max_profit_tradetwice(a):
    i, j = find_i_j(a)
    print("{0}:{1}".format(i, j))
    return max(max_profit(a), max_profit(a[:i + 1]) + max_profit(a[j:]))


print(max_profit([2, 5, 3, 6, 8, 1]))
print("---------")
print(max_profit_tradetwice([2, 5, 7, 100, 8, 2, 9]))
