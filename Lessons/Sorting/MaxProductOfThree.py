# def solution(A):
#     maxprod = float('-inf')
#     for i in range(len(A)-2):
#         for j in range(i+1,len(A)-1):
#             for k in range(j+1,len(A)):
#                 if maxprod < A[i]*A[j]*A[k]:
#                     maxprod = A[i]*A[j]*A[k]
#     return maxprod

def solution(A):
    SortedListA = sorted(A)
    ProductOptions = [SortedListA[-1]*SortedListA[-2]*SortedListA[-3], SortedListA[0]*SortedListA[1]*SortedListA[2], SortedListA[0]*SortedListA[1]*SortedListA[-1]]
    return(max(ProductOptions))

print( solution( [-5,-5,5,3] ) )