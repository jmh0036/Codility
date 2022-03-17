def solution(A):
    ListSetA = sorted(A)
    Length = len(ListSetA)
    if ListSetA == list(range(1,Length+1)):
        return 1
    else:
        return 0

print(solution ([1,2,3,1]))