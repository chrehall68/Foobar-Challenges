# thanks to stack overflow for finding this way of getting distinct
from datetime import datetime as d


class unique_element:
    def __init__(self, value, occurrences):
        self.value = value
        self.occurrences = occurrences


def perm_unique(elements):
    eset = set(elements)
    listunique = [unique_element(i, elements.count(i)) for i in eset]
    u = len(elements)
    return perm_unique_helper(listunique, [0] * u, u - 1)


def perm_unique_helper(listunique, result_list, d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d] = i.value
                i.occurrences -= 1
                for g in perm_unique_helper(listunique, result_list, d - 1):
                    yield g
                i.occurrences += 1


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
    all_layouts = tuple(perm_unique(layouts_lst))
    print(len(all_layouts))
    print(f"time taken was {(d.now()-start).total_seconds()}")
    print(all_layouts)


solution(2, 2, 2)


"""
might be helpful

After you edited your question, here is the new answer.

In order to solve this question, you should separate into different cases.

First, let's try to find all the 4-letter words that have different letters.

Like Debanjan pointed out, this leads to 8*7*6*5 = 1680 words. The idea for this is just to consider you have 8 possibilities for the first letter, but for the second letter you only have 7 possibilities since it must be different from the first one, and so on.

Now, let's count the word that have 2 "M", but all other letters are different. You have 7 choices for another letter, and 6 for the last letter. However, the 2 "M" might be anywhere in the word, thus you multiply this by the number of permutation, which is given by 4!2!2!=6 Thus, there are 7*6*6 = 252 such words.

[ EDIT: Here I need to explain something, as Ross commented out.

I only count 252 such words and not 504, because in the 42 choices of letters, I can choose "S" and "C", but I can also choose "C" and then "S". So either you have to divide the 7*6 by 2, or you only allow permutations that don't change the order of the first other letter chosen and the second other letter chosen.

Sorry, I didn't want to explain this in details, but it is true it is needed, in order to avoid confusion. ]

There are also 252 words with 2 "A" and all other letters different.

There are also 252 words with 2 "T".

Finally, there are 6 words with 2 "A" and 2 "M", 6 words with 2 "A" and 2 "T" and 6 words with 2 "M" and 2 "T".

Total: 1680 + 252 + 252 + 252 + 6 + 6 + 6
"""
