# 4-3-MissingInteger-try-1.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # if len(A) == 1:
    #     return
    
    A.sort()
    
    i = 0
    ans = 1
    while(i < len(A)):
        if A[i] < ans: # 比ans小不用看
            i = i + 1
        elif A[i] == ans:
            i = i + 1
            ans = ans + 1
        else: # A[i] > ans? 100 > 1
            return ans
            # pass
        
    return ans

# pass O(N) or O(N * log(N))