

def addition(num1, num2):
    answer = float(num1) + float(num2)
    return answer

def subtraction(num1, num2):
    answer = float(num1) - float(num2)
    return answer

def multiplation(num1, num2):
    answer = float(num1) * float(num2)
    return answer

def division(num1, num2):
    answer = float(num1) / float(num2)
    return answer

numbers = {}

game = True
# print(addition())
while game == True:
    names = list(numbers.keys())
    answers = list(numbers.values())

    decision = input("do you want to: \n\n1. perform an arithmetic operation\n2. retreive a stored value from the dictionary\n3. quit\n\nenter 1, 2, or 3: ")
    # arithmetic operation
    if decision == "1":
        answer = None
        operation = input("\nDo you want to add, subtract, multiply, or divide? ")

        num1 = input("\nenter your first number: ")
        num2 = input("enter your second number: ")
        
        if not isinstance(num1, float or int) or not isinstance(num2, float or int):
            print("invalid numbers")
            continue

        operation = operation.lower()

        if operation == "add" or 1:
            answer = addition(num1, num2)
            print("\nthe answer was", answer)
        elif operation == "subtract" or 2:
            answer = subtraction(num1, num2)
            print("\nthe answer was", answer)
        elif operation == "multiply" or 3:
            answer = multiplation(num1, num2)
            print("\nthe answer was", answer)
        elif operation == "divide" or 4:
            answer = division(num1, num2)
            print("\nthe answer was", answer)
        else:
            print("\ninvalid operation")

        name = input("\nwhat would you like to name this entry: ")

        numbers[name] = answer
        print("\nthis is the dictionary:", numbers, "\n")
    
    # retreave a stored value from a dictionary
    elif decision == "2":
        name = input("\nenter the name of the number you want to retreave: ")
        if name in names:
            numberIndex = names.index(name)
            print("the number set to", name, "is", answers[numberIndex])
        else:
            print("invalid")
    
    
    elif decision == "3":
        game = False
        print("Thanks!")

    else:
        print("invalid")