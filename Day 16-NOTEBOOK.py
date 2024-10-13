T = int(input())
for _ in range(T):
    N = int(input())
    total_pages = N * 1000
    notebooks = total_pages // 100
    print(notebooks)