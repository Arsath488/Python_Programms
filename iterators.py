from itertools import combinations


N = int(input())
letters = input().split()
K = int(input())


indices = list(range(N))
all_combinations = list(combinations(indices, K))

a_indices = {i for i, char in enumerate(letters) if char == 'a'}


favorable_outcomes = 0
for combo in all_combinations:
    if any(idx in a_indices for idx in combo):
        favorable_outcomes += 1

probability = favorable_outcomes / len(all_combinations)
print(f"{probability:.4f}")
