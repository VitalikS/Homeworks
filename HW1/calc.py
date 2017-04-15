
user_answer = input('Укажите какое действие вы хотите выполнить ( + - * / ^ ): ')
number1 = int(input('введите число 1: '))

if user_answer == '^':
    number2 = int(input('введите степень: '))
else:
    number2 = int(input('введите число 2: '))


if user_answer == '+':
    print(number2 + number1)
elif user_answer == '-':
    print(number1 - number2)
elif user_answer == '*':
    print(number2 * number1)
elif user_answer == '/':
    print(number1 / number2)
elif user_answer == '^':
    print(number1 ** number2)
else:
    print('wrong operation')