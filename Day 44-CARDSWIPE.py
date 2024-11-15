def max_people_in_office(test_cases):
    results = []
    
    for swipes in test_cases:
        current_people = set()
        max_people = 0
        current_count = 0
        
        for swipe in swipes:
            if swipe not in current_people:
                current_people.add(swipe)
                current_count += 1
                max_people = max(max_people, current_count)
            else:
                current_people.remove(swipe)
                current_count -= 1
        
        results.append(max_people)
    
    return results

T = int(input())
test_cases = []

for _ in range(T):
    N = int(input())
    swipes = list(map(int, input().split()))
    test_cases.append(swipes)

results = max_people_in_office(test_cases)

for result in results:
    print(result)