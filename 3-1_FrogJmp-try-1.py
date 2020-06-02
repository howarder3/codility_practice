# 3-1-FrogJmp-try-1.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    
    cnt = 0
    while(X<Y):
        Y = Y - D
        cnt += 1
        
    return cnt


# TLE O(Y-X)