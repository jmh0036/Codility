# def solution(X,A):
#     if set(range(1,X+1)).issubset((set(A))) == False:
#         return -1        
#     i = 0
#     Positions = A[:i]
#     while Positions != list(range(1,X+1)):
#         i+=1
#         Positions = list(set(A[:i]))
#     return i-1

def solution(X,A):
    if set(range(1,X+1)).issubset((set(A))) == False:
        return -1        
    i = 0
    Positions = []
    while Positions != list(range(1,X+1)):
        elt = A[i]
        if elt not in Positions:
            Positions.append(elt)
            Positions = sorted(Positions)
        i += 1
    return i-1

print( solution(5, [1,3,1,4,2,3,5,4]) )