from collections import Counter

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    max_freq = max(Counter(A).values())
    print(N - max_freq)