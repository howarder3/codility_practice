# 4-2-MaxCounters-try-1.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    
    num_list = [0] * N
    
    for i in range(len(A)):
        if A[i]>=1 and A[i] <= N:
            num_list[A[i]-1] += 1
        elif A[i] == N+1:
            num_list = [max(num_list)] * N
        else: # other case
            pass
        
        # print(num_list)
        
    return num_list
            
# TLE O(N*M)