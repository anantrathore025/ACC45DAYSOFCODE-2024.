def can_measure(W, X, Y, Z):
    weights = [X, Y, Z]
    combinations = []
    for i in range(2**len(weights)):
        combination = [weights[j] if (i & (1 << j)) else 0 for j in range(len(weights))]
        combinations.append(sum(combination))
    return W in combinations

T = int(input())
for _ in range(T):
    W, X, Y, Z = map(int, input().split())
    if can_measure(W, X, Y, Z):
        print("YES")
    else:
        print("NO")
