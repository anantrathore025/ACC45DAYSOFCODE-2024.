def can_candidate_a_win(test_cases):
    results = []
    
    for (N, X), A_votes, B_votes in test_cases:
        current_wins = sum(1 for i in range(N) if A_votes[i] > B_votes[i])
        needed_votes = [B_votes[i] - A_votes[i] + 1 for i in range(N) if A_votes[i] <= B_votes[i]]
        
        needed_votes.sort()
        
        for needed in needed_votes:
            if X >= needed:
                X -= needed
                current_wins += 1
            else:
                break
        
        results.append("YES" if current_wins > N // 2 else "NO")
    
    return results

T = int(input())
test_cases = []

for _ in range(T):
    N, X = map(int, input().split())
    A_votes = list(map(int, input().split()))
    B_votes = list(map(int, input().split()))
    test_cases.append(((N, X), A_votes, B_votes))

results = can_candidate_a_win(test_cases)
print("\n".join(results))