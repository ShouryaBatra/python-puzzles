def create_student_scores_dict(names, scores):
    student_scores = {}
    for i in range(len(names)):
        student_scores[names[i]] = scores[i]
    return student_scores

def get_average_score(student_scores):
    sum = 0
    scores = list(student_scores.values())
    for score in scores:
        sum = sum + score
    average = sum / len(scores)
    return average

def get_highest_scoring_student(student_scores):
    max = None
    maxIndex = None
    print(student_scores.values())
    values = list(student_scores.values())
    keys = list(student_scores.keys())
    for i in range(len(values)):
        if max == None or values[i] > max:
            maxIndex = i
            max = values[i]
    # return f"{keys[maxIndex]} scored the highest with a score of {max}"
    return keys[maxIndex]

def add_student_score(student_scores, name, score):
    student_scores[name] = score
    # return student_scores
    # dont actually need to return it because 
    # dictionaries arent cloned when they are passed into a function
    # they are passed by address/pointer

def remove_lowest_scoring_student(student_scores):
    values = list(student_scores.values())
    keys = list(student_scores.keys())
    min = None
    minIndex = None
    for i in range(len(values)):
        if min == None or values[i] < min:
            min = values[i]
            minIndex = i
    del student_scores[keys[minIndex]]
    return student_scores



names = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 92, 78, 95]

student_scores = create_student_scores_dict(names, scores)
print(student_scores)

# print(get_average_score(student_scores))
# print(get_highest_scoring_student(student_scores))
add_student_score(student_scores, 'Eva', 89)
# print(remove_lowest_scoring_student(student_scores))

print(student_scores)


# def addOne(num):
#     num += 1

# hi = 3
# addOne(hi)
# print(hi)
