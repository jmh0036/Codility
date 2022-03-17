def solution(A):
    PassingPairs = [(i,j) for i in range(len(A)) if A[i] == 0 for j in range(i,len(A)) if A[j] == 1]
    if len(PassingPairs) > 1000000000:
        return -1
    return len(PassingPairs)

# def solution(A):
#     PassingPairs = []
#     for i in range(len(A)-1):
#         for j in range(i,len(A)):
#             if A[i] == 0 and A[j] == 1:
#                 PassingPairs.append((i,j))
#     return len(PassingPairs)

print( solution([0,1,0,1,1]) )