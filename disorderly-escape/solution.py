import itertools
from datetime import datetime as d


def get_distinct(iterable):
    ret = set()
    for i in iterable:
        ret.add(i)
    return tuple(ret)


def solution(w, h, s):
    """
    @param w - width of the grid
    @param h - height of the grid
    @param s - the number of states that each cell can have
    """

    start = d.now()
    layouts_lst = []
    for i in range(s):
        layouts_lst.extend([i for l in range(w * h)])
    # print(layouts_lst)
    all_layouts = itertools.permutations(layouts_lst, w * h)
    all_layouts = tuple(all_layouts)
    all_layouts = get_distinct(all_layouts)
    print(len(all_layouts))
    print(all_layouts)
    print()

    # print()

    print(f"time taken was {(d.now()-start).total_seconds()}")


solution(2, 2, 2)
solution(2, 2, 3)
