# 5-2-GenomicRangeQuery-try-2.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    DNA_dict = {
        "A":1,
        "C":2,
        "G":3,
        "T":4
    }
    
    DNA_num_list = []
    for ele in S:
        DNA_num_list.append(DNA_dict[ele])
    
    # print(DNA_num_list)
    
    ans_list = []
    for i in range(len(P)):
        min_num = min(DNA_num_list[P[i]:Q[i]+1])
        # for j in range(P[i],Q[i]+1):
        #     min_num = min(min_num, DNA_num_list[j])
            
        ans_list.append(min_num)
        
    
    return ans_list

# TLE O(N * M)