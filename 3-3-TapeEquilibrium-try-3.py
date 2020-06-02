# 3-3-TapeEquilibrium-try-3.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    if len(A) == 2:
        return abs(A[1]-A[0])
    
    
    all_sum = sum(A)
    if abs(all_sum) == 0: # 不能全選 要interval
        min_ans = 999999999
    else:
        min_ans = abs(all_sum)   
    
        
    
    for i in range(len(A)-1): # 不能全選 要interval
        all_sum -= 2* A[i]
        # if abs(all_sum) > 0: # can not be 0
        min_ans = min(min_ans, abs(all_sum))

    return min_ans

# 不能全選 要interval