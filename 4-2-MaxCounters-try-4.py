# 4-2-MaxCounters-try-4.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    
    num_list = [0] * N
    max_flag = 0
    cur_max = 0
    
    for i in range(len(A)):
        if A[i]>=1 and A[i] <= N:
            if num_list[A[i]-1] <= max_flag: # 未更新至最大
                num_list[A[i]-1] = max_flag + 1
            else:
                num_list[A[i]-1] += 1 # 有更新過 自己+1就可
            cur_max = max(cur_max, num_list[A[i]-1])  # 紀錄當前最大
        elif A[i] == N+1:
            max_flag = cur_max # 減少這部分的更新次數, 目前大家最少應該都要有 max_flag
        else: # other case
            pass
        
        
    for i in range(N): # 最後一次更新全部, 需全部至少都有 max_flag 值以上   
        if num_list[i] < max_flag:
            num_list[i] = max_flag
        
        # print(num_list)
        
    return num_list

# TLE O(N + M) # 減少更新次數