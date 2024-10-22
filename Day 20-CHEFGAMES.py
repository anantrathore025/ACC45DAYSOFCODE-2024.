def chefland_game(test_cases):
    results = []
    for case in test_cases:
        if all(r == 0 for r in case):
            results.append("IN")
        else:
            results.append("OUT")
    return results

def main():
    T = int(input()) 
    test_cases = []
    
    for _ in range(T):
        decisions = list(map(int, input().split()))
        test_cases.append(decisions)
    
    results = chefland_game(test_cases)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()