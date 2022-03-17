First = 1073741727
Second = 1073741631
Third = 1073741679

# First = 0
# Second = 0
# Third = 0

def LeadingZeroes(BinaryNumber, DesiredLength):
    return [0] * (DesiredLength - len(BinaryNumber)) + [int(i) for i in BinaryNumber]

def CountConformal(BinaryNumber):
    return 2**BinaryNumber.count(0)

def DomOnes(ListOfBinaries):
    WhereOnes = [0] * 30
    for i in range(30):
        for BinInt in ListOfBinaries:
            if BinInt[i] == 1:
                WhereOnes[i] = 1
    return WhereOnes

def solution(A, B, C):
    BinA = LeadingZeroes([int(i) for i in bin(A)[2:]],30)
    BinB = LeadingZeroes([int(i) for i in bin(B)[2:]],30)
    BinC = LeadingZeroes([int(i) for i in bin(C)[2:]],30)
    ConformToA = CountConformal(BinA)
    ConformToB = CountConformal(BinB)
    ConformToC = CountConformal(BinC)

    ConformToAandB = CountConformal(DomOnes([BinA,BinB]))
    ConformToAandC = CountConformal(DomOnes([BinA,BinC]))
    ConformToBandC = CountConformal(DomOnes([BinB,BinC]))

    ConformToABandC = CountConformal(DomOnes([BinA,BinB,BinC]))

    return ConformToA+ConformToB+ConformToC-ConformToAandB-ConformToAandC-ConformToBandC + ConformToABandC

print(solution(First,Second,Third))