T = int(input())

for _ in range(T):
    N = int(input())
    
    if N <= 1:
        print("no")
    elif N <= 3:
        print("yes")
    elif N % 2 == 0:
        print("no")
    else:
        is_prime = True
        for i in range(3, int(N**0.5) + 1, 2):
            if N % i == 0:
                is_prime = False
                break
        if is_prime:
            print("yes")
        else:
            print("no")