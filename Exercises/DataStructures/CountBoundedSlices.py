def solution(K, A):
    LenA = len(A)
    BoundedSlices = 0
    for start in range(LenA-1):
        for end in range(start+1,LenA):
            Slice = A[start:end+1]
            # print(Slice, start, end)
            if max(Slice) - min(Slice) <= K:
                BoundedSlices += 1
                # print(Slice, start, end)
                if BoundedSlices >= 1000000000:
                    return 1000000000
            else:
                break
    return BoundedSlices+LenA

DemoList = [3,5,7,6,3]
Bound = 2
# DemoList = [1000000000, 1000000000]
# Bound = 0
print( solution(Bound, DemoList) )