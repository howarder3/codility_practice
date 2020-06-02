# 4-1-FrogRiverOne-try-1.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    # if N == 1:
        
    # if X == 1:
    
    path = [i for i in range(1, X+1)] # all path 0~X
    # print(path)
    
    for i in range(len(A)):
        if A[i] in path: # get target path
            path.remove(A[i])
        else:
            pass
        
        # print(path)
        if len(path) == 0: # check the path
            return i
            
    return 0 # not found

# TLE 