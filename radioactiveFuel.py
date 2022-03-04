import numpy


def check(one_d_m):
    for item in one_d_m:
        if round(item) != round(item, 10):
            return False
    return True


def LCD(one_d_m):
    scalar = 1
    while not check(one_d_m * scalar):
        scalar += 1
    return scalar


def solution(m):
    initial_terminal = False
    if sum(m[0]) == 0:
        initial_terminal = True
    absorbing = []
    transient = []

    for row in m:
        if sum(row) == 0:
            absorbing.append(row)
        else:
            transient.append(numpy.array(row, dtype="float64") / sum(row))

    if initial_terminal:
        return [1] + [0] * (len(absorbing) - 1) + [1]

    # so according to wikipedia
    # the probability of any absorbing state
    # is B[i][j] given i initial state and j absorbing state

    # Q = transient by transient matrix
    # R = transient by absorbing matrix
    # N = (I-Q)^-1
    # B = N*R

    Q = numpy.array(transient)[:, : len(transient)]
    R = numpy.array(transient)[:, len(transient) :]
    N = numpy.linalg.inv(numpy.identity(Q.shape[0]) - Q)
    B = numpy.dot(N, R)

    # we do B[0] because B[0] gives probabilities given that initial state is state 0
    denominator = LCD(B[0])
    ret = []
    for num in B[0] * denominator:
        ret.append(int(round(num)))
    ret.append(denominator)
    return ret


print(
    solution(
        [
            [0, 1, 0, 0, 0, 1],
            [4, 0, 0, 3, 2, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
    )
)
