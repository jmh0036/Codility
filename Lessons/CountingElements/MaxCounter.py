def solution(N,A):
    counters = [0] * N
    for a in A:
        print(counters)
        if a in range(N+1):
            counters[a-1] += 1
        else:
            counters = [max(counters)] * N
    return counters

print(solution(1,[1,1,1,1,1]))