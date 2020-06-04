# 6-1-PassingCars-try-1.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if len(A) == 0: # N=0
        return 0
    if len(A) == 1: # N=1
        return 1
    if len(A) == 2: # N=2
        if A[0]==A[1]:
            return 1
        else:
            return 2
    
    
    A.sort()
    cnt = 0
    i = 0
    while(i<len(A)-1):
        # last compare: i= len-2 , len-1(max)
        while(A[i]==A[i+1] and i < len(A)-2): # max i = len-3 
            # last compare: i= len-2 , len-1(max)
            i += 1 # pass same until A[i]!=A[i+1]
        # count last distinct
        cnt += 1
        i += 1
        
        
    if A[-2]!=A[-1]: # last two not same
        cnt += 1
    
    return cnt
    
    
    # if A[-2] = A[-1] 
    # cnt + A[-1]
    
    # if A[-2] != A[-1] 
    # cnt + A[-2]
            
            
    # for i in range(len(A)):
    #     if A[i] != A[i+1] and safe_flag == 0: # find distinct
    #         return A[i]
    #     elif A[i] != A[i+1] and safe_flag == 1: # change value
    #         safe_flag = 0
    #     elif A[i] == A[i+1]:
    #         safe_flag = 1
            
        
    # if A[-2] != A[-1] # last num
    #     return A[-1]


# pass O(N*log(N)) or O(N)