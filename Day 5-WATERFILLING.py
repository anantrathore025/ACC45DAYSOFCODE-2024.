T = int(input())

for _ in range(T):
    B1, B2, B3 = map(int, input().split()) 
    
    print("Water filling time" if sum(x == 0 for x in [B1, B2, B3]) >= 2 else "Not now")