the_end = ""
while True:
    if the_end == 'yes':
        break
    input_num = input('Введите целое или вещественное число: ')

    try:
        float(input_num)
        print('Correct')
    except ValueError:
        print('Wrong')
    the_end = input(f'Завершить работу? (для завершения введите "yes"): ')
