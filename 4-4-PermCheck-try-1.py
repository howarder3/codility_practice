# 4-4-PermCheck-try-1.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    A.sort()
    
    i = 0
    while(i<len(A)):
        if A[i] == i+1: # start from 1 = A[0]
            i += 1
        else:
            return 0
    
    return 1 # no problem


# pass O(N) or O(N * log(N))
