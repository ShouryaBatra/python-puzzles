def create_student_scores_dict(names, scores):
    student_scores = {}
    for i in range(len(names)):
        student_scores[names[i]] = scores[i]
    return student_scores

def get_average_score(student_scores):
    sum = 0
    values = list(student_scores.values())
    for i in range(len(student_scores)):
        sum = sum + values[i]
    average = sum / len(values)
    return average

def get_highest_scoring_student(student_scores):
    max = None
    values = list(student_scores.values())
    keys = list(student_scores.keys())
    for i in range(len(values)):
        if max == None or values[i] > max:
            maxIndex = i
            max = values[i]
    return f"{keys[maxIndex]} scored the highest with a score of {max}"





names = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 92, 78, 95]

print(create_student_scores_dict(names, scores))


student_scores = create_student_scores_dict(names, scores)

print(get_average_score(student_scores))
print(get_highest_scoring_student(student_scores))
# print(list(student_scores.values())[0])