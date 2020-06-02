# 3-1-FrogJmp-try-2.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6

    # no steps, same position
    if X==Y:
        return 0
    
    # step >= 1
    cnt_step = 0
    while(X<Y): # X==Y 也算到
        step = 1
        Y = Y - D*step  # 每次至少小走一步
        cnt_step = cnt_step + step
        
        # print(Y)
        
        # speed up
        while(Y - D*step > X): # 能加倍減(加速走路)
            Y = Y - D*step
            cnt_step = cnt_step + step
            step = step << 1 # (乘2)
      
    return cnt_step 


# O(1) pass