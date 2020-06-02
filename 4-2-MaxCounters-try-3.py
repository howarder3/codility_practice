# 4-2-MaxCounters-try-3.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    
    num_list = [0] * N
    maxcnt = 0
    
    for i in range(len(A)):
        if A[i]>=1 and A[i] <= N:
            num_list[A[i]-1] += 1
            maxcnt = max(maxcnt, num_list[A[i]-1]) 
        elif A[i] == N+1:
            num_list = [maxcnt] * N
        else: # other case
            pass
        
        # print(num_list)
        
    return num_list

# TLE O(N + M)