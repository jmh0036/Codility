import math

def solution(N):
    NumOfFactors = 0
    for i in range( 1, int( math.sqrt(N) ) + 1 ):
        if N%i == 0 and N//i != i:
            print(i, N//i)
            NumOfFactors += 2
        if N%i == 0 and N//i == i:
            print(N//i)
            NumOfFactors += 1
    return NumOfFactors

print( solution( 24 ) )