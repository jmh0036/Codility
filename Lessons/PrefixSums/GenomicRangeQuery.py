def solution(S,P,Q):
    ImpactFactor = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    Answers = []
    lenP = len(P)
    lenQ = len(Q)
    for queries in range(min(lenP,lenQ)):
        Sequence = [ImpactFactor[S[i]] for i in range( min(P[queries],Q[queries]),max(P[queries],Q[queries])+1 )]
        Answers.append(min(Sequence))
    return Answers

print(solution( 'CAGCCTA',[2,5,0],[4,5,6] ))