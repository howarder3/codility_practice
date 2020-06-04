# 5-3-MinAvgTwoSlice-try-2.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # only slice 2,3, if slice > 4 can be 2,2
    
    if len(A) == 2:
        return 0
    
    avg_2_list = []
    avg_3_list = []
    
    for i in range(len(A)-2):
        avg_2_list.append((A[i]+A[i+1])/2)
        avg_3_list.append((A[i]+A[i+1]+A[i+2])/3)
    
    avg_2_list.append((A[-2]+A[-1])/2)
    
    if min(avg_3_list) > min(avg_2_list): # 2 比較小
        return avg_2_list.index(min(avg_2_list))
    elif min(avg_3_list) == min(avg_2_list): # 一樣小，傳回小index
        return min(avg_2_list.index(min(avg_2_list)),avg_3_list.index(min(avg_3_list)))
    else: # 3 比較小
        return avg_3_list.index(min(avg_3_list))
    

# pass O(N) # only slice 2,3, if slice > 4 can be 2,2