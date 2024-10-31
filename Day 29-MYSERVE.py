T = int(input())

for _ in range(T):
    P, Q = map(int, input().split())
    
    total_points = P + Q
    
    serve_number = total_points + 1
    
    if (serve_number - 1) // 2 % 2 == 0:
        print("Alice")
    else:
        print("Bob")