from copy import copy
from itertools import permutations

# easy mode:
def possible_permutations(sequence_as_list):
    for x in permutations(sequence_as_list):
        yield list(x)


# # hard mode:
# def possible_permutations(sequence):
#     def recurse(sequence, target_idx, perm, used):
#         if perm is None:
#             perm = [0] * len(sequence)
#
#         if used is None:
#             used = [False] * len(sequence)
#
#         if target_idx == len(sequence):
#             yield copy(perm)
#             return
#
#         for i, x in enumerate(sequence):
#             if not used[i]:
#                 perm[target_idx] = x
#                 used[i] = True
#                 yield from recurse(sequence, target_idx + 1, perm, used)
#                 used[i] = False
#
#     return recurse(sequence, target_idx=0, perm=None, used=None)


print(list(possible_permutations([1, 2, 3])))