# 5-4-PassingCars-try-1.py


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    if len(A) == 1:
        return 0
    
    # count 1 backward
    count_1 = []
    cnt_1 = 0
    
    for i in range(len(A)-1,-1,-1):
        if A[i] == 1:
            cnt_1 += 1
        count_1.append(cnt_1)    
        
    count_1 = count_1[::-1]
     
            
    mysum = 0
    for i in range(len(A)):
        if A[i] == 0:
            mysum += count_1[i]
            if mysum > 1000000000:  
                return -1
        
    return mysum 
        
# A         0 1 0 1 1
# count_1  
# count_1   3 3 2 2 1
#           v   v


# pass O(N)