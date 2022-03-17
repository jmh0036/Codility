# def solution(A):
#     sortedA = sorted(A)
#     if len(sortedA) == 0:
#         return 0
#     i = 0
#     while sortedA.count(sortedA[i]) > 1:
#         i += sortedA.count(sortedA[i])
#         if i == len(sortedA):
#             return sorted[i]
#     return sortedA[i]

def solution(A):
    return len(set(A))

                
print(solution([2,1,1,2,3,1]))