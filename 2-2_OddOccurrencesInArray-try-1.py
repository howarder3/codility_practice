# 2-2_OddOccurrencesInArray-try-1

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    visited_twice = []
    visited_once = []
    
    for i in range(len(A)):
        if A[i] in visited_twice:
            pass
        elif A[i] in visited_once:
            visited_once.remove(A[i])
            visited_twice.append(A[i])
        else:
            visited_once.append(A[i])
            
            
    return visited_once[0]


# TLE O(N**2)

