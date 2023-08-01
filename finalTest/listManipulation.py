def get_average(numbers: list[float]) -> float:
    sum = 0
    for i in range(len(numbers)):
        sum = sum + numbers[i]
    average = sum / len(numbers)
    print(average)

get_average([2,4,6,8,10])
def get_max(numbers: list[int]) -> int:
    max = None
    for i in range(len(numbers)):
        if max == None or numbers[i] > max:
            max = numbers[i]
    print(max)
get_max([2,4,6,8,10])

def get_min(numbers: list[int]) -> int:
    min = None
    for i in range(len(numbers)):
        if min == None or numbers[i] < min:
            min = numbers[i]
    print(min)
get_min([2,4,6,8,10])

def get_even(numbers: list[int]) -> list[int]:
    evens = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            evens.append(numbers[i])
    print(evens)
get_even([3,12,7,6,9])
def get_odd(numbers: list[int]) -> list[int]:
    odds = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            odds.append(numbers[i])
    print(odds)
get_odd([3,12,7,6,9])
