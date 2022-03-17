GivenNumber = 15

def solution(N):
    BinString = bin(N)[2:]
    WhereOnes = []
    NextOne = 0
    i = 0
    while i  < len(BinString) and '1' in BinString[i:]:
        NextOne = BinString.index('1',i)
        WhereOnes.append(NextOne)
        i = NextOne+1
    MaxStringZeros = 0
    for i in range(len(WhereOnes)-1):
        CurrentZerosLength = WhereOnes[i+1] - WhereOnes[i]
        if CurrentZerosLength > MaxStringZeros:
            MaxStringZeros = CurrentZerosLength
    return max(0,MaxStringZeros-1)
    
print(bin(GivenNumber))
print(solution(GivenNumber))
