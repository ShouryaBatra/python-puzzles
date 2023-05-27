total_time = 60

pushup_counts = list(range(0, total_time + 1))

# print(pushup_counts)
scores = []

for num_pushups in pushup_counts:
    score = num_pushups * (total_time - num_pushups)
    scores.append(score)

scores.sort(reverse=True)
print(scores[0])
