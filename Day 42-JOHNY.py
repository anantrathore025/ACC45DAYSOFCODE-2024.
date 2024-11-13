T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    K = int(input())
    
    uncle_johny_length = A[K - 1]  
    
    sorted_A = sorted(A)
    
    new_position = sorted_A.index(uncle_johny_length) + 1    
    print(new_position)