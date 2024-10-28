T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    characteristic_values = list(map(int, input().split()))
    
    wolverine_count = 0
    
    for value in characteristic_values:
        if (value + K) % 7 == 0:
            wolverine_count += 1
    
    print(wolverine_count)