num = input("enter a positive integer greater than zero: ")
while not num.isdigit():
    print("your number doesn't meet the requirements!")
    num = input("enter a positive integer greater than zero: ")
num = int(num)
i = 0
sum = 0
while i <= num:
    sum = sum + i
    i = i + 2
print(sum)