# 1-1 BinaryGap


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def change_bin(x):
    bin_list = []
    maxcnt = 0
    cnt = -999
    while(x>0):
        next_digit = x%2
        if next_digit == 0: # case 0
            cnt = cnt + 1
        else: # case 1
            maxcnt = max(cnt, maxcnt)
            cnt = 0
        bin_list.append(next_digit) # 最右邊
        x = (x - (x%2))//2
        
    return max(0, maxcnt)
            
def solution(N):
    # write your code in Python 3.6
    max = -1
    

        # print(bin_list[::-1])
        
    maxcnt = change_bin(N)   
    return maxcnt
        
        
    # change_bin(17)
    # pass