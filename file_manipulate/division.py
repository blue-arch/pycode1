print('please give me two numbers!')
print('enter q to quit!')
while True:
    first_num = input('first number')
    if first_num=='q':
        break
    second_num = input('second number')
    if second_num=='q':
        break
    try:
        answer = float(first_num)/float(second_num)
        print(answer)
    except ZeroDivisionError:
        print("you can't divide by zero!")










