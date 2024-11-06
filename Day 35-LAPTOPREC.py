T = int(input())

for _ in range(T):
    N = int(input())
    
    recommendations = list(map(int, input().split())) 
    
    count = [0] * 11  
    
    for laptop in recommendations:
        count[laptop] += 1
    
    max_count = max(count)
    max_laptops = [i for i in range(1, 11) if count[i] == max_count]
    
    if len(max_laptops) > 1:
        print("CONFUSED")
    else:
        print(max_laptops[0])