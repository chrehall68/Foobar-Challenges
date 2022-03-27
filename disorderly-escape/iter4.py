import math


def solution(w, h, s):
    distinct = s ** (w * h)
    print("distinct states", distinct)
    total = 0
    for i in range(s - 1):
        for x in range(w * h + 1):
            temp = w - x + 1
            if (x - w) < 0:
                temp = x + 1
            total += math.comb(w * h, x) / temp
    print("total is ", total)


solution(2, 2, 2)
