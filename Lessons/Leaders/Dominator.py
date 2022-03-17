# def solution(A):
#     DesiredSize = len(A)//2
#     SetOfIntegers = set(A)
#     for i in SetOfIntegers:
#         if A.count(i) > DesiredSize:
#             return A.index(i)
#     return -1

def solution(A):
    LenA = len(A)
    DesiredLength = LenA//2
    if LenA == 0:
        return -1
    if LenA == 1:
        return 0
    EltZipIndex = []
    for i in enumerate(A):
        EltZipIndex.append([i[1],i[0]])
    EltZipIndex.sort()
    count = 1
    for idx in range(LenA-1):
        if EltZipIndex[idx][0] == EltZipIndex[idx+1][0]:
            count += 1
            if count > DesiredLength:
                return EltZipIndex[idx][1]
        else:
            count = 1
    return -1

# DemoList = [2,2,2,3,3,3,2,3,3,2]
DemoList = [3, 4, 3, 2, 3, -1, 3, 3]
# DemoList = [1]
# DemoList = []
print( solution(DemoList) )