import random

# def solution(A):
#     A.sort()
#     A.reverse()
#     for i in range(len(A)-1):
#         for j in range(i+1,len(A)):
#             for k in range(A[i]-A[j]+1,A[j]+1):
#                 if k in A[j+1:]:
#                     print(A[i],A[j],k)
#                     return 1
#     return 0

def solution(A):
    A.sort()
    A.reverse()
    posInd = 0
    while posInd < len(A) and A[posInd] > 0:
        posInd += 1
    A = A[:posInd]
    for i in range(len(A)-2):
        for j in range(i+1,len(A)-1):
            if A[i]-A[j] < A[j+1]:
                return 1
    return 0

experiment=[10,2,5,1,8,20]
# experiment = [random.choice([-1,1])*random.randint(0,2147483647) for i in range(10)]
# experiment = [5,3,3]
# experiment = [10, 50, 5, 1]

print(solution(experiment))