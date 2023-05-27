total_time = 60

pushup_counts = list(range(0, total_time + 1))

# print(pushup_counts)
best_score = 0
best_pushups = 0

for num_pushups in pushup_counts:
    score = num_pushups * (total_time - num_pushups)
    if score > best_score:
        best_score = score
        best_pushups = num_pushups

print(best_score, best_pushups)