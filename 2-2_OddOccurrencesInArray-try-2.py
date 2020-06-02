# 2-2-OddOccurrencesInArray-try-2.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    if len(A) == 1: # one number
        return A[0]
        
    A = sorted(A)
    i = 0
    while(i+1<len(A)):
        if A[i] == A[i+1]: # paired
            i = i + 2 
        else: # unpaired
            return A[i] 
            
    return A[i] # last one, unpaired

# O(N) or O(N*log(N)) pass
            