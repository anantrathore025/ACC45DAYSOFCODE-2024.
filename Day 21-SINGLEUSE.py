def minimum_attacks(test_cases):
    results = []
    for H, X, Y in test_cases:
        normal_attacks = (H + X - 1) // X
        health_after_special = H - Y
        total_attacks_with_special = 1 + (health_after_special + X - 1) // X if health_after_special > 0 else 1
        results.append(min(normal_attacks, total_attacks_with_special))
    return results

def main():
    T = int(input())
    test_cases = [tuple(map(int, input().split())) for _ in range(T)]
    results = minimum_attacks(test_cases)
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()