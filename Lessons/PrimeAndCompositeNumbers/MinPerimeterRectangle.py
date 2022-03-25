import math

def is_Prime(N):
    for i in range(2,int(math.sqrt(N))+1):
        if N%i == 0:
            return False
    return True

def solution(N):
    if is_Prime(N):
        return 2*N + 2
    CriticalPointRoundDown = int(math.sqrt(N))
    x = CriticalPointRoundDown
    while N%x != 0:
        x += 1
    y = N//x
    return 2*x + 2*y

print( solution( 15486451 ) )