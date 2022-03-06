"""
The below formulas are derived just from looking at many examples
and trying to match the examples to a formula

num_given = ( num_bunnies C num_required ) * num_required / num_bunnies
num_distinct = num_bunnies C (num_required-1)
uses_per_key = ( num_bunnies C num_required ) * num_required / num_distinct

4 bunnies, 2 required

4C1 = 4 distinct
4C2 * 2 / 4 = 3 -> 3 given
4C2 * 2 / 4 = 3 uses_per_key

0 2 3
0 1 3
1 2 3
0 2 1


4 bunnies, 1 required
4C0 = 1 distinct
4C1 * 1 / 4 = 1 -> 1 given
4C1 * 1 / 1 = 4 uses_per_key

0
0
0
0


4 bunnies, 3 required
4C2 = 6 distinct
4C3 * 3 / 4 = 3 -> 3 given
4C3 * 3 / 6 = 4 * 3 / 6 = 2 uses_per_key

0 1 2
0 2 3
3 4 5
1 4 5


5 bunnies, 3 required
5C2 = 10 distinct
5C3 * 3 / 5 = 10*3/5 = 6 given
5C3 * 3 / 10 = 3 uses_per_key

0 1 2 3 4 5
0 1 2 6 7 8
0 3 4 6 7 9
1 3 5 6 8 9
2 4 5 7 8 9


2 bunnies, 2 required
2C1 = 2 distinct
2C2 * 2 / 2 = 1 given
2C2 * 2 / 2 = 1 uses_per_key

0
1


3 bunnies, 2 required
3C1 = 3 distinct
3C2 * 2 / 3 = 3 * 2 / 3 = 2 given
3C2 * 2 / 3 = 2 uses_per_key

0 1
0 2
1 2
"""


import math

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

    def __str__(self):
        ret = "["
        for i in self.key_list:
            ret += "(" + str(i) + "), "
        ret += "]"
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

    ret = [[] for i in range(num_buns)]

    # len(ret[i]) == num_given
    # each number appears uses_per_key times
    # there are distinct_keys different keys
    distinct_keys = math.comb(num_buns, num_required - 1)
    num_given = math.comb(num_buns, num_required) * num_required / num_buns
    uses_per_key = math.comb(num_buns, num_required) * num_required / distinct_keys

    keys = KeyList(distinct_keys)
    for i in range(num_buns):
        if i == 0:
            ret[i] = [keys.get_next() for i in range(int(num_given))]
            print(keys)

    print("there should be", distinct_keys, "distinct keys")
    print("give each bunny", num_given, "key(s)")
    print("each key should appear", uses_per_key, "times")
    print(ret)
    print()

    return ret


solution(5, 3)
solution(3, 2)
solution(4, 1)
solution(4, 4)
solution(5, 4)

"""
distinct_keys = math.comb(num_buns, num_required)
    used = {}
    unused = {}
    for overlap in range(9):
        for keys_to_give in range(math.factorial(num_buns)):
            used = {0: [i for i in range(distinct_keys)]}
            for i in range(1, overlap + 1):
                used[i] = []
            ret[0] = [i for i in range(keys_to_give)]
            for num in ret[0]:
                used[0].remove(num)
                used[1].append(num)

            for i in range(1, num_buns):
                prev = ret[i - 1]
                for t in range(overlap):
                    # for now, assert that overlap and times used are equal
                    prev[t] = used
    # so maybe we can iterate over distinct keys
    # and iterate through given keys

"""
