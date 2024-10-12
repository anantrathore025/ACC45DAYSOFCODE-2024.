import math

T = int(input())
for _ in range(T):
    N, K, M = map(int, input().split())
    capacity = K * M
    bags_needed = math.ceil(N / capacity)
    print(bags_needed)