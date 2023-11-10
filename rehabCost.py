def recur_cost(lst, x, y, pos, curr_cost, count, memo):
    minm_cost = 2 ** 32
    if (pos, count) in memo:
        return memo[(pos, count)]

    if pos >= len(lst) and count == 0:
        return curr_cost

    if pos >= len(lst):
        return minm_cost

    if count == 0:
        return curr_cost

    curr = recur_cost(lst, x, y, pos + y, lst[pos] + curr_cost, count - 1, memo)
    skip_curr = recur_cost(lst, x, y, pos + 1, 0, x, memo)
    minm_cost = min(minm_cost, min(curr, skip_curr))
    memo[(pos, count)] = minm_cost
    return minm_cost


def minm_rehab_cost_r(lst, x, y):
    memo = {}
    ans = recur_cost(lst, x, y, 0, 0, x, memo)
    print(ans)

minm_rehab_cost_r([4, 2, 5, 4, 3, 5, 1, 4, 2, 7], 3, 2)