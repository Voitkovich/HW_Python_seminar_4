# ДЗ Семинар 4.

# Вычислить число c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# import math 
# pi = print(math.pi)

# from math import pi

# d = int(input("Введите число для заданной точности числа Пи: "))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')



# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# num = int(input("Введите число: "))
# i = 2  # первое простое число
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {old} приведены в списке: {lst}")

# n = int(input("Введите число: ")) 
# my_list = []
# num = 2
# while num <= n:
#         if n % num == 0:
#             my_list.append(num)
#             n //= num
#             num = 2
#         else:
#             num += 1    
# print(my_list)

# Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной последовательности.

# numbers = input("Введите числа через пробел:\n").split()
# print(f"Исходный список: {numbers}")
# new_lst = []
 
# for new_lst in new_lst:
#         if numbers not in new_lst:
#            new_lst.append(numbers)
# print(*new_lst)


# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")

import numpy as N
list_inp = input("Введите числа через пробел:\n").split() 
res = N.array(list_inp)
unique_res = N.unique(res) 
print("Список неповторяющихся элементов с использованием библиотеки numpy.unique():\n")
print(unique_res)
