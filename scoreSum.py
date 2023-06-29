"""
read a text file 
inside the text file there are a list of peoples names and their score
input format:

shourya 2
kabir 69
shourya 420
rajni 5

if there are duplicate names, it is the same person and you must add their scores for their total
print out the three people and their scores that have the highest scores

output format:

First place: shourya 422
Second place: kabir 69
Third place: rajni 5
"""

counterDictionary = {}

# TODO

sortedList = sorted(counterDictionary.items(), key=lambda x: x[1], reverse=True)

firstPlace = sortedList[0]
print(firstPlace[0] + "'s score was " + str(firstPlace[1]))
