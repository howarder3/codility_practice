# 5-2-GenomicRangeQuery-try-3.py

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
    last_1_list = []
    last_2_list = []
    last_3_list = []
    last_4_list = []
    last_1_idx = -1
    last_2_idx = -1
    last_3_idx = -1
    last_4_idx = -1
    
    for i in range(len(S)):
        DNA_num_list.append(DNA_dict[S[i]])
        if DNA_num_list[i] == 1:
            last_1_idx = i
        elif DNA_num_list[i] == 2:
            last_2_idx = i
        elif DNA_num_list[i] == 3:
            last_3_idx = i  
        elif DNA_num_list[i] == 4:
            last_4_idx = i
            
        last_1_list.append(last_1_idx)
        last_2_list.append(last_2_idx)
        last_3_list.append(last_3_idx)
        last_4_list.append(last_4_idx)
        
    
    # print(DNA_num_list)
    
    ans_list = []
    for i in range(len(P)):
        start_idx = P[i]
        last_idx = Q[i]
        if last_1_list[last_idx] >= start_idx and last_1_list[last_idx] != -1: 
            # 找到最後一個1的idx，如果idx超過起點，就是1
            ans_list.append(1)
        elif last_2_list[last_idx] >= start_idx and last_2_list[last_idx] != -1:  
            # 找到最後一個2的idx，如果idx超過起點，就是2
            ans_list.append(2)
        elif last_3_list[last_idx] >= start_idx and last_3_list[last_idx] != -1:  
            # 找到最後一個3的idx，如果idx超過起點，就是3
            ans_list.append(3)
        else:  # 找到最後一個4的idx，如果idx超過起點，就是4
            ans_list.append(4)
        # min_num = min(DNA_num_list[P[i]:Q[i]+1])
        # for j in range(P[i],Q[i]+1):
        #     min_num = min(min_num, DNA_num_list[j])

    return ans_list

# pass O(N + M) # 在搜尋一次中 順便記錄所有答案所需要的資訊， 也就是說 在特定idx的查詢能得到更多資訊