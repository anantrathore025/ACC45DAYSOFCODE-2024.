T = int(input())

for _ in range(T):
    N, A, B = map(int, input().split())
    
    rounds = 0
    while N > 1:
        N //= 2
        rounds += 1
    
    total_time = rounds * A + (rounds - 1) * B
    
    print(total_time)