T = int(input())

for _ in range(T):
    N = int(input())  
    
    A = list(map(int, input().split())) 
    
    count1 = A.count(1)
    count_neg1 = A.count(-1)
    
    total_sum = count1 - count_neg1
    
    if total_sum % 2 != 0:
        print(-1)
    else:
        flips = abs(total_sum) // 2
        print(flips)