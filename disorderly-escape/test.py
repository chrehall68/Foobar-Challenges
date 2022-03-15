import math


def solution(l, w, s):
    # pascal's triangle stuff
    triangle_level = l + w + (s - 1)
    coefficients = []
    for i in range(triangle_level):
        coefficients.append(math.comb(triangle_level - 1, i))
    print(coefficients)
    print(sum(coefficients))
    return sum(coefficients)


rolling_count = 0
for i in range(15):
    rolling_count += solution(0, 0, i + 1)
    print("rolling count is", rolling_count)
    print()

# (2, 2, 2) -> 7
# (2, 3, 4) -> 430

#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
# (2, 2, 3) -> 27
