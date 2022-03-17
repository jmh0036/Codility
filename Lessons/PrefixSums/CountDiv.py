# def solution(A,B,K):
    # NumberDiv = 0
    # for i in range(A,B+1):
    #     if i%K == 0:
    #         NumberDiv +=1
    # return NumberDiv

def solution(A,B,K):
    epsilon = 0
    if B-A == 0 and B%K == 0:
        return 1
    else:
        if (B-A+1)%K != 0:
            for i in range(B,B-((B-A+1)%K),-1):
                if i%K == 0:
                    epsilon = 1
                    break
        return ((B-A+1)//K)+epsilon

# print(solution(6,11,2))
print(solution(11,345,17))