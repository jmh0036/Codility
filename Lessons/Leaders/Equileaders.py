def leader(A):
    B = A.copy()
    LenB = len(B)
    DesiredLength = LenB//2
    if LenB == 1:
        return B[0]
    B.sort()
    count = 1
    for idx in range(LenB-1):
        if B[idx] == B[idx+1]:
            count += 1
            if count > DesiredLength:
                return B[idx]
        else:
            count = 1
    return 0.5

def solution(A):
    LenA = len(A)
    if len(set(A)) == 1:
        return LenA -1
    Dominator = leader(A)
    if Dominator == 0.5:
        return 0
    FirstSlice = [A[0]]
    SecondSlice = A[1:]
    if FirstSlice[0] == Dominator:
        FirstDomCount = 1
    else:
        FirstDomCount = 0
    SecondDomCount = SecondSlice.count(Dominator)
    LenFirst = 1
    LenSecond = LenA-1
    equileaders = 0
    for i in range(LenA-1):
        if FirstDomCount > LenFirst//2 and SecondDomCount > LenSecond//2:
            equileaders += 1
        FirstSlice.append(SecondSlice.pop(0))
        LenFirst += 1
        LenSecond -= 1
        if FirstSlice[-1] == Dominator:
            FirstDomCount += 1
            SecondDomCount -= 1
    return equileaders


DemoList = [4,3,4,4,4,2]

print(DemoList)
print( solution(DemoList) )