def solution(A):
    minAvg = float("inf")
    position = 0
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            CurrentAvg = sum(A[i:j+1])/(j-i+1)
            if CurrentAvg < minAvg:
                minAvg = CurrentAvg
                position = i
    return position

print(solution([4,2,2,5,1,5,8]))