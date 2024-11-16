def calculate_min_coins(N):
    full_sets = N // 5
    remaining_gifts = N % 5
    total_coins = (full_sets * 4) + remaining_gifts
    return total_coins

T = int(input())
results = []

for _ in range(T):
    N = int(input())
    results.append(calculate_min_coins(N))

for result in results:
    print(result)