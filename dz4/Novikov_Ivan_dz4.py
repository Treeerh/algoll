from random import randint, random

import cProfile


def foo():
    f_array = [randint(-20, 20) for i in range(20)]
    li = []
    [li.append(x) for x in f_array if x not in li]
    return li


# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего
#     задания первых трех уроков.
#     Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
#   3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
#   O(n)
def mm_arr(random_array):
    a = random_array.index(max(random_array))
    a1 = max(random_array)
    b = random_array.index(min(random_array))
    b1 = min(random_array)
    random_array[a] = b1
    random_array[b] = a1
    print(b, b1, '-------', a, a1)
    return random_array


def mm_arr_for(random_arr):
    mm = 0
    mm_i = 0
    mx = 0
    mx_i = 0
    for i in range(0, len(random_arr)):
        if random_arr[i] > mx:
            mx = random_arr[i]
            mx_i = i
        if random_arr[i] < mm:
            mm = random_arr[i]
            mm_i = i
    random_arr[mm_i] = mx
    random_arr[mx_i] = mm
    print(mm_i, mm, '-----', mx_i, mx)
    return random_arr


def mm_arr_while(random_arr):
    mm = 0
    mm_i = 0
    mx = 0
    mx_i = 0
    i = 0
    while i < len(random_arr):
        if random_arr[i] > mx:
            mx = random_arr[i]
            mx_i = i
        if random_arr[i] < mm:
            mm = random_arr[i]
            mm_i = i
        i += 1
    random_arr[mm_i] = mx
    random_arr[mx_i] = mm
    print(mm_i, mm, '-----', mx_i, mx)
    return random_arr


def main():
    random_array = foo()
    mm_arr(random_array)
    mm_arr_for(random_array)
    mm_arr_while(random_array)


# cProfile.run('main()')

# при формировании списка -20 до 20  без повторений
# 7 -19 ------- 6 16  0.0 time
# 6 -19 ----- 7 16    0.0 time
# 7 -19 ----- 6 16    0.0 time
# 179 function calls in 0.000 seconds
# 1 0.000 0.000 0.000 0.000 < string >: 1( < module >)
# 1 0.000 0.000 0.000 0.000 Novikov_Ivan_dz4.py: 15(mm_arr)
# 1 0.000 0.000 0.000 0.000 Novikov_Ivan_dz4.py: 25(mm_arr_for)
# 1 0.000 0.000 0.000 0.000 Novikov_Ivan_dz4.py: 42(mm_arr_while)
# 1 0.000 0.000 0.000 0.000 Novikov_Ivan_dz4.py: 5(foo)
# при формировании списка -200 до 200  без повторений
# 136 -199 ------- 92 198   0.0 time
# 92 -199 ----- 136 198     0.0 time
# 136 -199 ----- 92 198     0.0 time
# 1398 function calls in 0.001 seconds
# 1 0.000 0.000 0.000 0.000 Novikov_Ivan_dz4.py: 15(mm_arr)
# 1 0.000 0.000 0.000 0.000 Novikov_Ivan_dz4.py: 25(mm_arr_for)
# 1 0.000 0.000 0.000 0.000 Novikov_Ivan_dz4.py: 42(mm_arr_while)
# 1 0.000 0.000 0.001 0.001 Novikov_Ivan_dz4.py: 5(foo)
# при формировании списка -2000 до 2000   без повторений
# 1544 -1996 ------- 881 1998   0.0009999275207519531 time
# 881 -1996 ----- 1544 1998     0.0 time
# 1544 -1996 ----- 881 1998     0.0 time
# 13203 function calls in 0.030 seconds
# 1 0.000 0.000 0.000 0.000 Novikov_Ivan_dz4.py: 15(mm_arr)
# 1 0.000 0.000 0.000 0.000 Novikov_Ivan_dz4.py: 25(mm_arr_for)
# 1 0.000 0.000 0.001 0.001 Novikov_Ivan_dz4.py: 42(mm_arr_while)
# 1 0.000 0.000 0.029 0.029 Novikov_Ivan_dz4.py: 5(foo)
# при формировании списка -20000 до 20000   без повторений
# 1887 -19999 ------- 337 19996   0.00099945068359375 time
# 337 -19999 ----- 1887 19996     0.0019979476928710938 time
# 1887 -19999 ----- 337 19996     0.004998922348022461 time
# 144104 function calls in 2.674 seconds
# 1 0.000 0.000 0.001 0.001 Novikov_Ivan_dz4.py: 15(mm_arr)
# 1 0.001 0.001 0.001 0.001 Novikov_Ivan_dz4.py: 25(mm_arr_for)
# 1 0.004 0.004 0.005 0.005 Novikov_Ivan_dz4.py: 42(mm_arr_while)
# 1 0.000 0.000 2.667 2.667 Novikov_Ivan_dz4.py: 5(foo)
# при формировании списка -200000 до 200000   без повторений
# 11655 -200000 ------- 112592 199996  0.013977766036987305 time
# 112592 -200000 ----- 11655 199996    0.013991355895996094 time
# 11655 -200000 ----- 112592 199996    0.05297064781188965 time
# 1377093 function calls in 278.777 seconds
# 1 0.000 0.000 0.013 0.013 Novikov_Ivan_dz4.py: 15(mm_arr)
# 1 0.014 0.014 0.014 0.014 Novikov_Ivan_dz4.py: 25(mm_arr_for)
# 1 0.038 0.038 0.052 0.052 Novikov_Ivan_dz4.py: 42(mm_arr_while)
# 1 0.000 0.000 278.692 278.692 Novikov_Ivan_dz4.py: 5(foo)
# Сами ф-и линецны O(n)
# уское горлышко ф-я foo , а точнее исключение повторений, имеет сложность O(n^2) квадратичная

# if __name__ == '__main__':
#     print("# 3==========================")
#     random_array = foo()
#     start = time.time()
#     # print(random_array)
#     mm_arr(random_array)
#     finish = time.time()
#     print(finish - start,'time')
#     start1 = time.time()
#     # print(random_array)
#     mm_arr_for(random_array)
#     finish1 = time.time()
#     print(finish1 - start1, 'time')
#     start2 = time.time()
#     # print(random_array)
#     mm_arr_while(random_array)
#     finish2 = time.time()
#     print(finish2 - start2, 'time')
# --------------------------------------------------------------------------

# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
#     Без использования «Решета Эратосфена»;
#     Используя алгоритм «Решето Эратосфена»
#     Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
#     Результаты анализа сохранить в виде комментариев в файле с кодом.

def eratosfen(n):
    a = [i for i in range(n + 1)]
    a[1] = 0
    i = 2
    # return a
    while i < n ** 0.5:
        if a[i] != 0:
            j = i ** 2
            while j <= n:
                a[j] = 0
                j = j + i
        i = i + 1
    a = set(a)
    a.remove(0)
    b = sorted(list(a))
    return b

def numbers(n):
    ar = []
    for i in range(2, n + 1):
        k = 0
        for j in range(1, i + 1):
            if i % j == 0:
                k = k + 1
        if k == 2:
            ar.append(i)
    return ar





def main1():
    n = int(input())
    print(eratosfen(n))   # Сложность O(n)
    print(numbers(n))     # Сложность O(n^2)

cProfile.run('main1()')
# n = 10
# 1 0.000 0.000 0.000 0.000 Novikov_Ivan_dz4.py: 151(eratosfen)
# 1 0.000 0.000 0.000 0.000 Novikov_Ivan_dz4.py: 168(numbers)
# n = 100
# 1 0.000 0.000 0.000 0.000 Novikov_Ivan_dz4.py: 151(eratosfen)
# 1 0.000 0.000 0.000 0.000 Novikov_Ivan_dz4.py: 168(numbers)
# n = 1000
# 1    0.000    0.000    0.000    0.000 Novikov_Ivan_dz4.py:151(eratosfen)
# 1    0.022    0.022    0.022    0.022 Novikov_Ivan_dz4.py:168(numbers)
# n = 10000
# 1    0.002    0.002    0.002    0.002 Novikov_Ivan_dz4.py:151(eratosfen)
# 1    2.547    2.547    2.547    2.547 Novikov_Ivan_dz4.py:168(numbers)

