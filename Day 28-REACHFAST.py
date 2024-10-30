T = int(input())

for _ in range(T):
    A, B, K = map(int, input().split())
    
    distance = abs(A - B)
    
    steps = (distance + K - 1) // K     
    print(steps)