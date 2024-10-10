T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    if (Y / X) * 100 >= 50:
        print("YES")
    else:
        print("NO") 
