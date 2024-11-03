N = int(input())

cumulative_score_player1 = 0
cumulative_score_player2 = 0
max_lead = 0
winner = 0

for _ in range(N):
    S, T = map(int, input().split())
    cumulative_score_player1 += S
    cumulative_score_player2 += T
    
    if cumulative_score_player1 > cumulative_score_player2:
        current_lead = cumulative_score_player1 - cumulative_score_player2
        current_winner = 1
    else:
        current_lead = cumulative_score_player2 - cumulative_score_player1
        current_winner = 2
    
    if current_lead > max_lead:
        max_lead = current_lead
        winner = current_winner

print(winner, max_lead)