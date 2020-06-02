# 3-2-PermMissingElem-try-1.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 1

    A.sort()
    
    i = 0
    while(i < len(A)):
        if i+1 == A[i]:
            i = i + 1
        else:
            return i+1
            
    return i+1

# O(N) or O(N * log(N)) pass