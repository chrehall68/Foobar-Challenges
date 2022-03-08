import itertools
import math


def comb(n, r):
    return math.factorial(n) / (math.factorial(n - r) * math.factorial(r))


def solution(num_buns, num_required):
    # case where num_buns == num_required
    if num_buns == num_required:
        return [[i] for i in range(num_buns)]
    # case where num_required == 1
    if num_required == 1:
        return [[0] for i in range(num_buns)]
    # no bunnies required, so don't need to give anything
    if num_required == 0:
        return []

    # len(ret[i]) == num_given
    # each number appears uses_per_key times
    # there are distinct_keys different keys
    distinct_keys = comb(num_buns, num_required - 1)
    num_given = comb(num_buns, num_required) * num_required / num_buns
    uses_per_key = comb(num_buns, num_required) * num_required / distinct_keys
    num_given, uses_per_key = int(num_given), int(uses_per_key)

    # so previous plan of finding itertools.combinations(range(distinct_keys), num_given)
    # and then going through them is too slow

    # so we want to give num_given keys to each bunny
    # so we want to find how many ways we can give keys to each assuming
    # that you can use it only uses_per_key_times.
    # So instead, we find the combos for which bunnies can have the distinct
    # keys
    # Then, we can give keys based on these bunnies that have distinct keys
    iters = itertools.combinations(range(num_buns), uses_per_key)

    # the combinations of (range(num_buns), uses_per_key) yields
    # the bunnies to give the distinct keys to
    # so now all we need to do is to just give the distinct keys
    ret = [[] for i in range(num_buns)]
    for i in range(distinct_keys):  # give out the distinct keys
        for bunny in next(iters):  # to each bunny that gets it
            ret[bunny].append(i)  # bunny is an idx

    # the lists should already be sorted since we add 0's first, then 1's, etc
    return ret
