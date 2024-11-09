def max_distance(T, test_cases):
    results = []
    for N, M, A in test_cases:
        total_distance = sum(max(M - a, a - 1) for a in A)
        results.append(total_distance)
    return results


T = int(input())
test_cases = [tuple(map(int, input().split())) + (list(map(int, input().split())),) for _ in range(T)]

for result in max_distance(T, test_cases):
    print(result)