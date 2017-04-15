# Задача: реализовать игру в загадки
# Требования:
#	Программа выводить в консоль текст загадки и ждать ввода пользователя
#	Программа после ввода пользователя ответа должна вывести в консоль результат: правильный ли ответ дал пользователь
#	Загадок должно быть 10, тематика вопросов должна быть по первому занятию
#	Программа должна в конце игры сказать, сколько ответов дал пользователь: сколько из них было верных
#	Программа должна не учитывать регистр ответа: "Python" и "python" оба должны быть правильным ответом на вопрос "Какой язык мы учим?"

# Переменные
# список вопросов
# qt_1    = q-uestion_t-ext_#

qt_1 = ('Какой язык мы изучаем? ')
qt_2 = ('Как зовут нашего преподавателя? ')
qt_3 = ('С какой версией Python мы работаем? ')
qt_4 = ('К какому типу данных относится число 17? ')
qt_5 = ('К какому типу данных относится число 13.14151617? ')
qt_6 = ('Какой еще числовой тип данных существует? ')
qt_7 = ('Как обозначается тип даных "Ничего"? ')
qt_8 = ('Какую кодировку разработали как новый международный стандарт передачи символов? ')
qt_9 = ('Какие два основных способа управления логикой программы? (напишите через запятую) ')
qt_10 = ('Спомощью какой команды задаются "Перебирающие" циклы? ')

# список ответов
# cat_1_1	= c-orrct_a-nswer_t-ext_#question_#answer

cat_1_1 = ('python')
cat_1_2 = ('Python')
cat_1_3 = ('pyton')
cat_1_4 = ('Питон')
cat_2_1 = ('Никита')
cat_2_2 = ('никита')
cat_2_3 = ('Nikita')
cat_2_4 = ('nikita')
cat_3_1 = ('3.6')
cat_3_2 = ('3,6')
cat_3_3 = ('3.6')
cat_3_4 = ('3,6')
cat_4_1 = ('int')
cat_4_2 = ('INT')
cat_4_3 = ('Int')
cat_4_4 = ('инт')
cat_5_1 = ('float')
cat_5_2 = ('Float')
cat_5_3 = ('FLOAT')
cat_5_4 = ('флоат')
cat_6_1 = ('complex')
cat_6_2 = ('Complex')
cat_6_3 = ('Комплексный')
cat_6_4 = ('комплексный')
cat_7_1 = ('None')
cat_7_2 = ('none')
cat_7_3 = ('NONE')
cat_7_4 = ('ноне')
cat_8_1 = ('Unicode')
cat_8_2 = ('unocode')
cat_8_3 = ('utf-8')
cat_8_4 = ('UTF-8')
cat_9_1 = ('loops, conditions')
cat_9_2 = ('conditions, loops')
cat_9_3 = ('Условия, циклы')
cat_9_4 = ('Циклы, условия')
cat_10_1 = ('For')
cat_10_2 = ('for')
cat_10_3 = ('FOR')
cat_10_4 = ('фор')

# Другие
user_score = 0
quatity_rounds = 10
numb_correct_ans = 0
numb_wrong_ans = 0
Python = python = 1

# приветики
username_input = input('Как тебя зовут? ')
while True:
    wannagame_input = input('Привет, %s! Хочешь сыграем в игру? Press Y/N ' % username_input)
    if str(wannagame_input) == 'Y':
        print('Ура ура, давай начнем')
        # игра
        print('Сейчас я задам тебе 10 вопросов, ответы на них будут односложными (состоять из одного слова)')
        # Вопросы
        uat_1 = input(qt_1)
        uat_2 = input(qt_2)
        uat_3 = input(qt_3)
        uat_4 = input(qt_4)
        uat_5 = input(qt_5)
        uat_6 = input(qt_6)
        uat_7 = input(qt_7)
        uat_8 = input(qt_8)
        uat_9 = input(qt_9)
        uat_10 = input(qt_10)
        # Проверка
        # вопрос1
        if uat_1 == cat_1_1:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 1: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_1 == cat_1_2:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 1: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_1 == cat_1_3:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 1: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_1 == cat_1_4:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 1: Правильно, 1 балл. ИТОГО %s' % user_score)
        else:
            numb_wrong_ans = numb_wrong_ans + 1
            print('Вопрос 1: Неправильно, 0 баллов. ИТОГО %s' % user_score)
        # вопрос2
        if uat_2 == cat_2_1:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 2: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_2 == cat_2_2:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 2: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_2 == cat_2_3:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 2: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_2 == cat_2_4:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 2: Правильно, 1 балл. ИТОГО %s' % user_score)
        else:
            numb_wrong_ans = numb_wrong_ans + 1
            print('Вопрос 2: Неправильно, 0 баллов. ИТОГО %s' % user_score)
        # вопрос3
        if uat_3 == cat_3_1:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 3: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_3 == cat_3_2:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 3: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_3 == cat_3_3:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 3: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_3 == cat_3_4:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 3: Правильно, 1 балл. ИТОГО %s' % user_score)
        else:
            numb_wrong_ans = numb_wrong_ans + 1
            print('Вопрос 3: Неправильно, 0 баллов. ИТОГО %s' % user_score)
        # вопрос4
        if uat_4 == cat_4_1:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 4: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_4 == cat_4_2:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 4: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_4 == cat_4_3:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 4: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_4 == cat_4_4:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 4: Правильно, 1 балл. ИТОГО %s' % user_score)
        else:
            numb_wrong_ans = numb_wrong_ans + 1
            print('Вопрос 4: Неправильно, 0 баллов. ИТОГО %s' % user_score)
        # вопрос5
        if uat_5 == cat_5_1:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 5: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_5 == cat_5_2:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 5: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_5 == cat_5_3:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 5: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_5 == cat_5_4:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 5: Правильно, 1 балл. ИТОГО %s' % user_score)
        else:
            numb_wrong_ans = numb_wrong_ans + 1
            print('Вопрос 5: Неправильно, 0 баллов. ИТОГО %s' % user_score)
        # вопрос6
        if uat_6 == cat_6_1:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 6: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_6 == cat_6_2:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 6: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_6 == cat_6_3:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 6: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_6 == cat_6_4:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 6: Правильно, 1 балл. ИТОГО %s' % user_score)
        else:
            numb_wrong_ans = numb_wrong_ans + 1
            print('Вопрос 6: Неправильно, 0 баллов. ИТОГО %s' % user_score)
        # вопрос7
        if uat_7 == cat_7_1:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 7: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_7 == cat_7_2:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 7: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_7 == cat_7_3:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 7: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_7 == cat_7_4:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 7: Правильно, 1 балл. ИТОГО %s' % user_score)
        else:
            numb_wrong_ans = numb_wrong_ans + 1
            print('Вопрос 7: Неправильно, 0 баллов. ИТОГО %s' % user_score)
        # вопрос8
        if uat_8 == cat_8_1:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 8: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_8 == cat_8_2:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 8: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_8 == cat_8_3:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 8: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_8 == cat_8_4:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 8: Правильно, 1 балл. ИТОГО %s' % user_score)
        else:
            numb_wrong_ans = numb_wrong_ans + 1
            print('Вопрос 8: Неправильно, 0 баллов. ИТОГО %s' % user_score)
        # вопрос9
        if uat_9 == cat_9_1:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 9: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_9 == cat_9_2:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 9: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_9 == cat_9_3:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 9: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_9 == cat_9_4:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 9: Правильно, 1 балл. ИТОГО %s' % user_score)
        else:
            numb_wrong_ans = numb_wrong_ans + 1
            print('Вопрос 9: Неправильно, 0 баллов. ИТОГО %s' % user_score)
        # вопрос10
        if uat_10 == cat_10_1:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 10: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_10 == cat_10_2:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 10: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_10 == cat_10_3:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 10: Правильно, 1 балл. ИТОГО %s' % user_score)
        elif uat_10 == cat_10_4:
            user_score = user_score + 1
            numb_correct_ans = numb_correct_ans + 1
            print('Вопрос 10: Правильно, 1 балл. ИТОГО %s' % user_score)
        else:
            numb_wrong_ans = numb_wrong_ans + 1
            print('Вопрос 10: Неправильно, 0 баллов. ИТОГО %s' % user_score)
        # total_score
        if user_score >= 7:
            print('{}, молодец! продолжай в том же духе! Ты ответил на {} вопросов правильно'.format(username_input,
                                                                                                     numb_correct_ans))
        elif user_score >= 5:
            print(
            '{}, ты ответил правильно всего на {} вопросов, не увывай и продолжай дальше. У тебя получится!'.format(
                username_input, numb_correct_ans))
        else:
            print('Попробуй ещё раз, запусти игру заново')
        break
    elif str(wannagame_input) == 'N':
        print('Ну ничего, приходи в другой раз')
        break
    else:
        print ('Попробуй еще раз! Нажми  Y или N ')
        continue