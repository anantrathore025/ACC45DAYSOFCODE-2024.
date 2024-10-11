T = int(input())
for _ in range(T):
    a, b, c, d = map(int, input().split())
    max_ab = max(a, b)
    max_cd = max(c, d)
    print(max_ab + max_cd)