T = int(input())

for _ in range(T):
    N, X, Y = map(int, input().split())
    
    max_score = N * X
    
    if Y <= max_score and Y % X == 0:
        print("YES")
    else:
        print("NO")