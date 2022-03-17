def solution(A):
    # for i in range(1,len(A)+2):
    #     if i not in A:
    #         return i
    A = sorted(A)
    Size = len(A)
    if 1 not in A:
        return 1
    if A[-1] == Size:
        return Size+1
    for i in range(Size-1):
        if A[i+1]-A[i] != 1:
            return A[i]+1

print(solution([2,3,1,5]))