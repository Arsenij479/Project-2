import random


start = input('Вы запустили игру "Камень, ножницы, бумага". Хотите поиграть? (Вводите + или -): ')

if start == '+':
    print('Загрузка...')
    print('Если захотите закончить вводите "-".')
    print('Если захотите узнать счёт вводите "с".')
    user_ball = 0
    rand_ball = 0
    while True:
        user = input("Камень, ножницы или бумага?  ")
        list_play = ['камень', 'ножницы', 'бумага']
        if user in list_play:
            rand = random.choice(list_play)
            print(rand)

            if rand == 'камень' and user == 'ножницы':
                rand_ball += 1
            if rand == 'камень' and user == 'бумага':
                user_ball += 1
            if rand == 'ножницы' and user == 'камень':
                user_ball += 1
            if rand == 'ножницы' and user == 'бумага':
                rand_ball += 1
            if rand == 'бумага' and user == 'ножницы':
                user_ball += 1
            if rand == 'бумага' and user == 'камень':
                rand_ball += 1
        elif user == 'с':
            print('Ваши баллы - ', user_ball, '. Баллы вашего соперника - ', rand_ball, ".")
        elif user == '-':
            print('Ваши баллы - ', user_ball, '. Баллы вашего соперника - ', rand_ball, ".")
            print('Конец игры! Заходите ещё!')
            break
        else:
            print('Вводите камень, ножницы или бумагу')


if start == '-':
    print('Жаль... :(')
else:
    print('Простите, я вас не понял, если хотите играть перезапустите программу и введите "+". Спасибо!')