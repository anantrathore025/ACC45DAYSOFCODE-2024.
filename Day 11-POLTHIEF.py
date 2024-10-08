T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    diff = abs(X - Y)
    print(diff) 