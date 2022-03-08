import math
import random
import numpy


def is_valid(l, uses_per_key, num_required, num_distinct):
    flattened = numpy.array(l).flatten().tolist()
    print(flattened)
    for i in range(max(flattened) + 1):
        if flattened.count(i) != uses_per_key:
            return False

    # make sure that it doesn't work with
    # num_required - 1 bunnies
    valid_ones = find_all_combos(len(l), num_required)
    invalid_ones = find_all_combos(len(l), num_required - 1)
    for combo in valid_ones:
        a = set()
        for idx in combo:
            a.update(set(l[idx]))
        truths = [i in a for i in range(num_distinct)]
        print("valid", truths)
        if not all(truths):
            return False

    for combo in invalid_ones:
        a = set()
        for idx in combo:
            a.update(set(l[idx]))
        truths = [i in a for i in range(num_distinct)]
        print("invalid", truths)
        if all(truths):
            return False  # we don't want i-1 to be able to do it

    return True


def find_all_combos(num_buns, num_req):
    ret = []
    choices = [i for i in range(num_buns)]
    cur = []
    total_num = math.comb(num_buns, num_req)
    found = 0
    while found != total_num:
        temp = choices.copy()
        cur = []
        for i in range(num_req):
            cur.append(temp.pop(random.randint(0, len(temp) - 1)))
        if cur not in ret:
            ret.append(cur)
            found += 1
    return ret


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
    distinct_keys = math.comb(num_buns, num_required - 1)
    num_given = math.comb(num_buns, num_required) * num_required / num_buns
    uses_per_key = math.comb(num_buns, num_required) * num_required / distinct_keys
    num_given, uses_per_key = int(num_given), int(uses_per_key)

    print()
    print("there should be", distinct_keys, "distinct keys")
    print("give each bunny", num_given, "key(s)")
    print("each key should appear", uses_per_key, "times")
    print("possible layouts are", find_all_combos(num_buns, num_required))

    # so this time I'll place the first, and every time you place a new one,
    # make sure that it doesn't work with n-1 groups

    if num_required <= 3:
        # see "intersection.png" for why I do this
        # if |a U b U c| = n, then |a U b| <= n-1
        # in our case, n should be distinct_keys

        goal_union_magnitude = distinct_keys - 1

        # solve the equation to find the particular solution such that |a U b| == n-1
        intersection_mag = 0
        each_set_distinct_mag = 0

        for intersection in range(num_given + 1):
            each_set_distinct_mag = num_given - intersection
            if (
                intersection + each_set_distinct_mag * num_required
                == goal_union_magnitude
            ):
                intersection_mag = intersection
                break

        # use the intersection mag to fill the rest
        intersection_mag


solution(6, 4)
