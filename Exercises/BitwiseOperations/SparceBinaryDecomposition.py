def IsSparce(BinaryNumber):
    for i in range(len(BinaryNumber)-1):
        if BinaryNumber[i] == BinaryNumber[i+1] == '1':
            return False
    return True

def solution(N):
    for i in range(N//2+1):
        if IsSparce(bin(i)[2:]) and IsSparce(bin(N-i)[2:]):
            return i
    return -1

print(solution(74901729))