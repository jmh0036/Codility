def solution(A,K):
    return [ A[i-K] for i in range(len(A)) ]

print(solution([3, 8, 9, 7, 6],3))