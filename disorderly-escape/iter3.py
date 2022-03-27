def solution(w, h, s):
    distinct_states = s ** (w * h)
    print(distinct_states)


print(solution(2, 3, 2))
print(solution(2, 3, 4))

# width
# height
# states

# 2 2 2 -> 7 non-equal, 16 distinct (verified)
# 2 2 3 -> 27 non-equal, 81 distinct (verified)
# 2 3 4 -> 430 non-equal, 4096 distinct (verified)

# so num distinct = s^(w*h)
