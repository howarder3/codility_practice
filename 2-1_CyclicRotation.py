# 2-1 CyclicRotation

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    
    strlen = len(A)
    # K = K%strlen #5, 1=6
    ans = A.copy()
    
    for i in range(strlen):
        ans[(i+K)%strlen] = A[i]
        
    return ans
        