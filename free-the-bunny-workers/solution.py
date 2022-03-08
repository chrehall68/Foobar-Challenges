import math
import random
import numpy

# ok so the return value should be a list
# len(l) = num_bunnies


class Key:
    def __init__(self, value):
        self.value = value
        self.uses = 0

    def retrieve(self):
        self.uses += 1
        return self.value

    def __str__(self):
        return "key with value {} and {} uses".format(self.value, self.uses)

    def __eq__(self, o):
        return self.uses == o.uses and self.value == o.value

    def __lt__(self, o):
        if self.uses < o.uses:
            return True
        if self.uses > o.uses:
            return False
        return self.value < o.value

    def __le__(self, o):
        if self.uses < o.uses:
            return True
        if self.uses > o.uses:
            return False
        return self.value <= o.value

    def __gt__(self, o):
        if self.uses > o.uses:
            return True
        if self.uses < o.uses:
            return False
        return self.value > o.value

    def __ge__(self, o):
        if self.uses > o.uses:
            return True
        if self.uses < o.uses:
            return False
        return self.value >= o.value


class KeyList:
    def __init__(self, num_keys):
        self.key_list = [Key(i) for i in range(num_keys)]
        self.used_list = []

    def __getitem__(self, idx):
        ret = self.key_list[idx].retrieve()
        self.key_list.sort()
        self.used_list = [key for key in self.key_list if key.uses > 0]
        self.used_list.sort()
        return ret

    def get_next(self):
        ret = self.key_list[0].retrieve()
        if self.key_list[0] not in self.used_list:
            self.used_list.append(self.key_list[0])
        self.key_list.sort()
        self.used_list.sort()
        return ret

    def get_next_used(self):
        ret = self.used_list[0].retrieve()
        self.used_list.sort()
        self.key_list.sort()
        return ret

    def __str__(self):
        ret = "["
        for i in self.key_list:
            ret += "(" + str(i) + "), "
        ret += "]"
        return ret


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
    # take care of the easy cases first

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

    for overlap in range(num_given + 1):
        print("overlap is", overlap)
        ret = [[] for i in range(num_buns)]
        keys = KeyList(distinct_keys)
        for i in range(num_buns):
            if i == 0:
                ret[i] = [keys.get_next() for i in range(num_given)]
                # print(keys)
            else:
                # fill the current
                for x in range(overlap):
                    ret[i].append(keys.get_next_used())
                for o in range(overlap, num_given):
                    ret[i].append(keys.get_next())
        # print(ret)
        # print()

        # check if ret is valid
        if is_valid(ret, uses_per_key, num_required, distinct_keys):
            break
        print("failed with overlap", overlap, "and values", ret)
    else:
        ret = []
    # print(ret)

    # for row in ret:
    #    row.sort()

    return ret


"""print(solution(5, 3))
print(solution(3, 2))
print(solution(4, 1))
print(solution(4, 4))
print(solution(5, 4))
"""
# print(solution(4, 2))
print(solution(5, 3))

# find_all_combos(5, 3)
