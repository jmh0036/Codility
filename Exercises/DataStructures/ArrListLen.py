def solution(A):
    idx = 0
    pathLen = 1
    while A[idx] != -1:
        pathLen += 1
        idx = A[idx]
    return pathLen

DemoList = [1,4,-1,3,2]
print( solution(DemoList) )