# 5-1-CountDiv-try-1.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    
    # cnt = 0

    # for num in range(A,B+1): # A~B
    #     if num%K == 0:
    #         cnt += 1
    
    # return cnt
    # O(N)
    
    while(A%K != 0):
        A = A + 1 # 第一個 mod = 0 的 A
    
    while(B%K != 0):
        B = B - 1 # 最後一個 mod = 0 的 B
        
    ans = (B-A)//K +1
        
    # O(1)
            
            
    return ans