def solution(A):
    LenA = len(A)
    maxProfit = 0
    for i in range(LenA-1):
        for j in range(i+1,LenA):
            currentProfit = A[j]-A[i]
            if currentProfit > maxProfit:
                maxProfit = currentProfit
    return maxProfit

DemoList =[23171, 21011, 21123, 21366, 21013, 21367]

print( solution(DemoList) )