import itertools
import math
from tqdm import tqdm


def get_distinct(iterable):
    ret = set()
    for i in tqdm(iterable):
        ret.add(i)
    return tuple(ret)


def solution(w, h, s):
    """
    @param w - width of the grid
    @param h - height of the grid
    @param s - the number of states that each cell can have
    """

    if s == 0:
        return 1  # there's only one way to arrange it when there's only one state

    layouts_lst = []
    for i in range(s):
        layouts_lst.extend([i for l in range(w * h)])
    # print(layouts_lst)
    all_layouts = itertools.permutations(layouts_lst, w * h)
    print(math.perm(len(layouts_lst), w * h))
    all_layouts = get_distinct(all_layouts)
    print(len(all_layouts))
    print(all_layouts)
    print()

    # print()


if __name__ == "__main__":
    solution(2, 2, 2)
    solution(2, 2, 3)
    solution(2, 3, 2)
    solution(2, 3, 4)
