# def solution(A):
#     Intervals = []
#     for i in range(len(A)):
#         Intervals.append([max(0,i-A[i]),i+A[i]])
#     Intervals.sort()
#     Intersections = 0
#     for FirstCircleIdx in range(len(Intervals)-1):
#         for SecondCircleIdx in range(FirstCircleIdx+1,len(Intervals)):
#             if Intervals[FirstCircleIdx][1] >= Intervals[SecondCircleIdx][0]:
#                 Intersections += 1
#     return Intersections

def solution(A):
    Intervals = []
    for i in range(len(A)):
        Intervals.append([max(0,i-A[i]),i+A[i]])
    Intervals.sort()
    IntervalsLen = len(Intervals)
    Intersections = 0
    for FirstCircleIdx in range(len(Intervals)-1):
        SecondCircleIdx = FirstCircleIdx + 1
        while Intervals[FirstCircleIdx][1] >= Intervals[SecondCircleIdx][0] and Intersections <= 10000000:
            Intersections += 1
            SecondCircleIdx += 1
            if SecondCircleIdx > IntervalsLen - 1:
                break
        if Intersections > 10000000:
            return -1
    return Intersections


experiment=[1,5,2,1,4,0]
# experiment = [0] * 100

print(solution(experiment))
