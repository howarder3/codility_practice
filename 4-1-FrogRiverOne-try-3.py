# 4-1-FrogRiverOne-try-3.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):

    path_dict = {} 
    for i in range(1, X+1):
        path_dict[i] = -1

    checked_path = X
    for i in range(len(A)):
        if A[i] < X+1: # target range
            if path_dict[A[i]] == -1: # find dict, no path
                path_dict[A[i]] = 0
                checked_path = checked_path - 1
                
        if checked_path == 0:
            return i
            

        
    return -1 # -1 not found

# pass O(N)