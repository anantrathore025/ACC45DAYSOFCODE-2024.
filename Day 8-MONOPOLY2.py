T = int(input())  

for _ in range(T):
    P, Q, R, S = map(int, input().split())  

    sum_except_A = Q + R + S
    sum_except_B = P + R + S
    sum_except_C = P + Q + S
    sum_except_D = P + Q + R

    if P > sum_except_A or Q > sum_except_B or R > sum_except_C or S > sum_except_D:
        print("YES")  
        
    else:
        print("NO")  