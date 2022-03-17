def solution(A):
    ListSetA = sorted(list(set(A)))
    minA = min(ListSetA)
    maxA = max(ListSetA)
    if maxA < 1:
        return 1
    for i in range(1,maxA):
        if i not in ListSetA:
            return i
    return maxA+1

print( solution([-1,-3,3,4,5,6,7]) )