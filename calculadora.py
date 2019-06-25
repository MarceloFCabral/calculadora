def calculator():
    print('Wolf Blaze Productions')
    print('Welcome to A Simple Python Calculator!')
    num1 = input('Please insert the first number: ')
    while True:
        try:
            num1 = int(num1)
            break
        except:
            print("Please insert a valid number.")
            num1 = input('Please insert the first number: ')
    num2 = input('Please insert the second number: ')
    while True:
        try:
            num2 = int(num2)
            break
        except:
            print("Please insert a valid number.")
            num2 = input('Please insert the second number: ')
    operation_list = ['sum', 'subtraction', 'multiplication', 'division']
    operation = input('Which operation would you like to perform? ')
    while operation not in operation_list:
        print("You haven't typed in a valid arithmetic operation!")
        operation = input('Which operation would you like to perform? ')

    if operation == 'sum':
        result = num1 + num2
    elif operation == 'subtraction':
        result = num1 - num2
    elif operation == 'multiplication':
        result = num1 * num2
    else:
        result = num1 / num2

    print(f'The result of your operation is {result}')

    recalculate()


def recalculate():
    recalc = ''
    yesno = ['yes', 'no']
    while recalc not in yesno:
        recalc = input('Do you want to make another calculation? ')
    if recalc == 'yes':
        calculator()
    else:
        print('Thank you for using A Simple Python Calculator!')


calculator()
