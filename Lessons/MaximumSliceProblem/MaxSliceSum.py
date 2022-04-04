def solution(A):
    MaxSum = -1*float("inf")
    for i in range(len(A)):
        for j in range(i,len(A)):
            CurrentSum = sum(A[i:j+1])
            if CurrentSum > MaxSum:
                MaxSum = CurrentSum
    return MaxSum

Test = [3,2,-6,4,0]
print(solution(Test))