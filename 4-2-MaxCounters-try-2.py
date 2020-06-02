# 4-2-MaxCounters-try-2.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    
    
    num_dict = {}
    for i in range(N):
        num_dict[i] = 0
        
  
    maxcnt = 0
    
    for i in range(len(A)):
        if A[i]>=1 and A[i] <= N:
            num_dict[A[i]-1] += 1
            maxcnt = max(maxcnt, num_dict[A[i]-1])
        elif A[i] == N+1:
            # num_list = [maxcnt] * N
            for i in range(N):
                num_dict[i] = maxcnt
        else: # other case
            pass
        
        # print(num_dict.values())
        
    return list(num_dict.values())

# TLE O(N*M)