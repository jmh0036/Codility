# def solution(A):
#     MinDifference = float('inf')
#     for i in range(1,len(A)):
#         FirstPart = A[:i]
#         SecondPart = A[i:]
#         CurrentDifference = abs( sum(FirstPart) - sum(SecondPart) )
#         if MinDifference > CurrentDifference:
#             MinDifference = CurrentDifference
#     return MinDifference

def solution(A):
    PartialSums = []
    nextSum = 0
    for i in A:
        nextSum += i
        PartialSums.append(nextSum)
    Differences = []
    for i in range(len(PartialSums)-1):
        FirstHalf = PartialSums[i]
        SecondHalf = PartialSums[-1]-FirstHalf
        Differences.append(abs(FirstHalf-SecondHalf))
    return min(Differences)

print(solution([3,1,2,4,3]))