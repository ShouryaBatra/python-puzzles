def get_average(numbers: list[float]) -> float:
    sum = 0
    for i in range(len(numbers)):
        sum = sum + numbers[i]
    average = sum / len(numbers)
    return average

def get_max(numbers: list[int]) -> int:
    max = None
    for i in range(len(numbers)):
        if max == None or numbers[i] > max:
            max = numbers[i]
    return max

def get_min(numbers: list[int]) -> int:
    min = None
    for i in range(len(numbers)):
        if min == None or numbers[i] < min:
            min = numbers[i]
    return min

def get_even(numbers: list[int]) -> list[int]:
    evens = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            evens.append(numbers[i])
    return evens
    
def get_odd(numbers: list[int]) -> list[int]:
    odds = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            odds.append(numbers[i])
    return odds

# print(get_average([2,4,6,8,10]))
# print(get_max())
# print(get_min([2,4,6,8,10]))
# print(get_even([3,12,7,6,9]))
# print(get_odd([3,12,7,6,9]))

numbers1 = [2, 4, 6, 8, 10]

print(get_average(numbers1))
print(get_max(numbers1))
print(get_min(numbers1))
print(get_even(numbers1))
print(get_odd(numbers1))

print()
numbers2 = [3, 1, 7, 5, 9]

print(get_average(numbers2))
print(get_max(numbers2))
print(get_min(numbers2))
print(get_even(numbers2))
print(get_odd(numbers2))