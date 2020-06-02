# 3-3-TapeEquilibrium-try-4.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if len(A) == 2: # smallest case
       return abs(A[1]-A[0])
       
    
    r_sum_list = [0]
    r_sum = 0
    for r in range(len(A)):
        r_sum = r_sum + A[r]
        r_sum_list.append(r_sum)


    l_sum_list = [0]
    l_sum = 0
    for l in range(len(A)-1,-1,-1):
        l_sum = l_sum + A[l]
        l_sum_list.append(l_sum)

    # print(r_sum_list)
    # print(l_sum_list)
    all_sum_list = []
    for i in range(1, len(A)): # 1 ~ len(A)-1 # 不能全選，因為要interval
        all_sum_list.append(abs(r_sum_list[i] - l_sum_list[len(A)-i]))
        
    # print(all_sum_list)

    return min(all_sum_list)
    
    
    # 0 1 2 3 4 5 
    # 5 4 3 2 1 0

# O(N) # 不能全選，因為要interval