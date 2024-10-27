T = int(input())

for _ in range(T):
    N = int(input())
    strings = list(map(int, input().split()))
    
    total_skips = 0
    
    for i in range(1, N):
        total_skips += abs(strings[i] - strings[i - 1]) - 1
    
    print(total_skips)