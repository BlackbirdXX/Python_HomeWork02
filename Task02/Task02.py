# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import os
os.system("cls")

print("Программа, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.")

def number_input(input_string):
    while type:
        digit = input(input_string)
        try:
            digit = int(digit)
            return digit
        except ValueError:
            print("Введено неверное значение. Только числа!!!")

number_n = number_input('Введите число N : ')

def multiplication_factorial(digit):
    if digit < 0:
        digit*= -1
    factorial_array = []
    multi_factorial = 1
    for i in range(2, digit + 1):
        factorial_array.append(multi_factorial)
        multi_factorial *= i
        print(multi_factorial)

multiplication_factorial(number_n)