# def solution(A):
#     Elements = set(A)
#     for i in Elements:
#         if A.count(i)%2 != 0:
#             return i

# def solution(A):
#     idx = 0
#     while A.count(A[idx])%2 == 0:
#         A = [val for val in A if val != A[idx]]
#     return A[0]

def solution(A):
    return [i for i in A if A.count(i)%2 != 0][0]

print(solution([9,3,9,3,9,7,9]))