def solution(A,B):
    Living = []
    for i in range(len(A)):
        if Living == []:
            Living.append((A[i],B[i]))
        elif B[i] == Living[-1][1]:
            Living.append( (A[i],B[i]) )
        elif B[i] == 1 and Living[-1][1] == 0:
            Living.append( (A[i],B[i]) )
        elif Living[-1][1] == 1 and B[i] == 0:
            if Living[-1][0] < A[i]:
                Living[-1] = (A[i],B[i])
            while (len(Living) > 1) and (Living[-1][1] == 0 and Living[-2][1] == 1) and (Living[-1][0] > Living[-2][0]):
                Living.pop(-2)
            if (len(Living) > 1) and (Living[-1][1] == 0 and Living[-2][1] == 1) and (Living[-1][0] < Living[-2][0]):
                Living.pop(-1)
        # print(Living)
    return len(Living)

Fish = [1,3,2,5,4]
Direction = [1,1,0,0,0]
# Direction = [1,0,1,1,1]
# Fish = [1,2]
# Direction = [0,1]
print(solution(Fish,Direction))