# 4-1-FrogRiverOne-try-2.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    # if N == 1:
        
    # if X == 1:
    
    path_dict = {} 
    for i in range(1, X+1):
        path_dict[i] = -1
    # path = [i for i in range(1, X+1)] # all path 0~X
    # print(path)
    
    for i in range(len(A)):
        path_dict[A[i]] = 0
        # if A[i] in path: # get target path
        #     path.remove(A[i])
        # else:
        #     pass
        
        # print(path)
        # if len(path) == 0: # check the path
        #     return i
        
        # print(path_dict.values())
        if sum(path_dict.values()) == 0: # if = 0, found
            return i
            
    return -1 # -1 not found
    # if < 0, -1 not found
    # if = 0, found

# TLE O(N ** 2)