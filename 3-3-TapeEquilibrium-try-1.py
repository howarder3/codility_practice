# 3-3-TapeEquilibrium-try-1.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if len(A) == 2: # smallest case
       return abs(A[1]-A[0])
       
    
    # 概念: 負的視同丟到另外一邊的正, 全部轉正, 從大數開始處理
    for i in range(len(A)):
        if A[i] < 0:
            A[i] = -A[i]
            
    A.sort(reverse = True)
    
    group_a = A[0]
    group_b = A[1]
    
    i = 2
    while(i < len(A)):
        if group_a > group_b:
            group_b = group_b + A[i]
        else: 
            group_a = group_a + A[i]
            
        i = i + 1
        
    print(group_a, group_b)
    return abs(group_a - group_b)

# wrong ans 誤解題意
