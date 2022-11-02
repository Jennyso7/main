


# Задание №1
# Создайте класс Example. В нём пропишите 3 (метода) функции. Две
# переменные задайте статически, две динамически.
# Ȃервая функция: создайте переменную и выведите её
# Вторая функция: верните сумму 2-ух глобальных переменных
# Третья функция: верните результат возведения первой динамической
# переменной во вторую динамическую переменную
# Создайте объект класса.
# Ȁапечатайте обе функции
# Ȁапечатайте переменную a

# class Example:
#     static_v1 = 3
#     static_v2 = 7
#     def __init__(self):
#         self.dynamic_v1 = 5
#         self.dynamic_v2 = 2
#     def func_1(self):
#         new_v = 45
#         print(f" Создали новую переменную 'new_vf' со значением {new_v}")
#     def func_2(self):
#         return Example.static_v1 + Example.static_v2
#     def func_3(self):
#         return self.dynamic_v1 ** self.dynamic_v2
#
# class_object = Example()
# class_object.func_1()
# print(class_object.func_2())
# print(class_object.func_3())

# Задание №2
# Калькулятор.
# Создайте класс, где реализованы функции(методы) математических
# операций. А также функция, для ввод данных.

# class Calculator:
#     def __init__(self, input_num1, input_num2, input_oper):
#         self.input_num1 = int(input('Введите 1 число: '))
#         self.input_oper = input('Введите операцию(+,-,*,/): ')
#         self.input_num2 = int(input('Введите 2 число: '))
#
#     def plus(self):
#         return input_num1 + input_num2
#
#     def minus(self):
#         return input_num1 - input_num2
#
#     def pr(self):
#         return input_num1 * input_num2
#
#     def del_(self):
#         return input_num1 / input_num2
#
# class_object = Calculator()
# while True:
#     if self.input_oper == '+':
#         print(class_object.plus())
#
#     elif self.input_oper == '-':
#         print(class_object.minus())
#
#
#     elif self.input_oper == '*':
#         print(class_object.pr())
#     elif self.input_oper == '/':
#         print(class_object.del_())

# Домашнее задание
# Два метода в классе, один принимает в себя либо
# строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв
# меньше или равно длине слова, выводить все
# гласные, иначе согласные;
# если число то, произведение суммы чётных цифр
# на длину числа.
# Длину строки и числа искать во втором методе

class Way:
    def __init__(self, str_or_int):
        str_or_int = input("Введите слово: 'строка' либо 'число': ")
        vse_gls = ['а', 'о', 'е', 'и', 'я', 'ы', 'ю', 'э', 'у']
        gls = 0
        sgl = 0
        while True:
            if str_or_int == 'строка':
                str_ = input('Введите строку: ')
                print(str_)
                for i in str_:
                    if i in vse_gls:
                        gls += 1
                    else:
                        sgl +=1
                pr = gls * sgl
                        if pr <= len(str_):

                            print()
                        else:
                            print()
            elif str_or_int == 'число':
                int_ = int(input('Введите число: '))
                print(int_)
    def len_(self):



