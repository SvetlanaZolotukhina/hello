# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел
# будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введён
# после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить
# программу.
def our_sum(our_str, end):
    our_list = our_str.split( ) #склеиваем строку по пробелу в список
    sum_our_list = 0 #стартовое значение суммы
    for i in our_list:
        if i == end:
            break #если введем в список/строку/ якорное слово/значение для остановки
        sum_our_list += int(i) #добавляем целочисленное значение каждого элемента, это и будем выводить как итог
    return sum_our_list
#получила функцию, которая считает сумму введенных через пробел чисел, теперь нужен цикл со стоп-якорем
end = '0'
ending = False
l =0 #Значение суммы с которого начинает суммировать
while not ending:
    our_str = input('Введите числа через пробел, и я посчитаю их сумму, если достаточно, то введите 0: ')
    l += our_sum(our_str, end)
    ending = end in our_str
    print(f'Сумма введенных чисел: {l}')
print('Пока.') #ввод чисел и их суммирование продолжаются до стопа, вроде работает, но мне кажется что можно
# что-то еще додумать и дошлифовать
