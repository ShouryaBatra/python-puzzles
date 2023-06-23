# counter = 0

# num = input()

# anotherNum = num
# print(anotherNum)

# num = num.replace(" ", "")

# equationList = list(num)





# for i in range(int(num) - 1):
#     num = int(num) * (int(anotherNum) - i)

# num = num // int(anotherNum)

# print(num)


n = int(input())
# print(n)

answer = 1

for i in range(1, n + 1):
    answer *= i

print(answer)