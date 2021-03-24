# from collections import defaultdict
#
# n, m = map(int, input().split())
#
# groupA = list()
# groupB = list()
#
# for _ in range(n):
#     groupA.append(input())
#
# for _ in range(m):
#     groupB.append(input())
#
# # print(groupA)
# # print(groupB)
#
# for i in groupB:
#     if i not in groupA:
#         print(-1)
#
#     for en, j in enumerate(groupA, 1):
#         if i == j:
#             print(en, end=" ")
#     print()
#
#     # [print(en, end=" ") for en, j in enumerate(groupA, 1) if i == j]
#     # [print(-1, end=" ") for en, j in enumerate(groupA, 1) if i != j]

# =========================================================================

# Alternate solution

from collections import defaultdict

n,m = list(map(int,input().split()))
d = defaultdict(list)
for i in range(n):
    d[input()].append(i+1)
for i in range(m):
    print(*d[input()] or [-1])

    # What
    # does * in Python
    # mean?
    #
    # The * in python is used
    # to
    # unpack
    # the
    # iterable.
    #
    # print(*[1, 2, 3])
    # # 1 2 3
    #
    # print(*(1, 2, 3))
    # # 1 2 3
    #
    # print(*"123")
    # # 1 2 3
    # The or condition
    # returns
    # the
    # first
    # true
    # value
    #
    # print(0 or 1 or 2)
    # # 1
    #
    # print(1 or 0 or 2)
    # # 1
    #
    # print("" or 0 or "Good")
    # # Good
    #
    # print([] or [-1])
    # # [-1]
    # When
    # d[input()] is empty
    # its
    # value
    # will
    # be[]
    #
    # print(*d[input()] or [-1])
    # So
    # our
    # above
    # code
    # evaluates
    # to
    #
    # print(*[] or [-1])
    # The * is evaluated
    # at
    # last.First
    # it
    # will
    # evaluate[] or [-1].So
    # our
    # code
    # becomes
    #
    # print(*[-1])
    # # -1

