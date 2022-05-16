from random import randint, random

def foo():
    f_array = [randint(-20, 20) for i in range(20)]
    li = []
    [li.append(x) for x in f_array if x not in li]
    return li

def fooo():
    f_array = [randint(-20, 20) for i in range(40)]
    return f_array

# 1. В диапазоне натуральных чисел от 2 до 99 определить,
#     сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
def multiplicity():
    rez=[]
    for j in range(2,10):
        s=0
        for i in range(2,100):
            if i%j==0:
                s=s+1
        rez.append(s)
    return rez

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
#     Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
#     то во второй массив надо заполнить значениями 1, 4, 5, 6
#     (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях
#     первого массива стоят четные числа.
def even_array(f_array):
    e_array=[]
    for i in range(len(f_array)):
        if f_array[i]%2==0:
            e_array.append(i)
    return e_array

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
def mm_arr(random_array):
    a=random_array.index(max(random_array))
    a1 = max(random_array)
    b=random_array.index(min(random_array))
    b1 = min(random_array)
    random_array[a]=b1
    random_array[b]=a1
    return random_array

# 4. Определить, какое число в массиве встречается чаще всего.
def freq_arr(n_array):
    mass=[]
    for i in n_array:
        s=n_array.count(i)
        mass.append(s)
    a=mass.index(max(mass))
    return F'val = {n_array[a]}'

# 5. В массиве найти максимальный отрицательный элемент.
#     Вывести на экран его значение и позицию в массиве.
def max_min_in_arr(q_arr):
    g_array= {}
    for i in range(len(q_arr)):
        if q_arr[i]<0:
            g_array[i]=q_arr[i]
    v=max(g_array.values())
    k=list(g_array.keys())[list(g_array.values()).index(v)]
    return F'key ={k}   val={v}'

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и
#     максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
def sum_array(mass_ar):
    sum=0
    max_in_arr=max(mass_ar)
    min_in_arr=min(mass_ar)
    a = mass_ar.index(max_in_arr)
    b = mass_ar.index(min_in_arr)
    if a > b:
        for i in range(b+1,a):
            sum=sum+mass_ar[i]
    else:
        for i in range(a+1,b):
            sum=sum+mass_ar[i]
    return F'min = {min_in_arr} max = {max_in_arr} a = {a} b = {b} sum = {sum}'

# 7. В одномерном массиве целых чисел определить два наименьших элемента.
#     Они могут быть как равны между собой (оба являться минимальными), так и различаться.
def min_t_arr(e_arr):
    e_arr.sort()
    return F'{e_arr[0]} {e_arr[1]}'

# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
#     Программа должна вычислять сумму введенных элементов каждой строки и записывать
#     ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
def matrix():
    matr=[]
    for i in range(4):
        f = list(map(int, input('Введите 4 числа через пробел ').split()))
        f.append(sum(f))
        matr.append(f)
    return matr

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
def max_matrix():
    matr = []
    for i in range(5):
        f = [randint(-20, 20) for i in range(5)]
        matr.append(f)
    print(matr)
    max_0 = -21
    for j in range(5):
        min_0 = 21
        for i in range(5):
            if matr[i][j] < min_0:
                min_0 = matr[i][j]
        if min_0 > max_0:
            max_0 = min_0
    return max_0




if __name__ == '__main__':
    print("# 1==========================")
    print(multiplicity())
    print("# 2==========================")
    f_array = foo()
    print(f_array)
    print(even_array(f_array))
    print("# 3==========================")
    random_array = foo()
    print(random_array)
    print(mm_arr(random_array))
    print("# 4==========================")
    ran_arr = fooo()
    print(ran_arr)
    print(freq_arr(ran_arr))
    print("# 5==========================")
    f_array = foo()
    print(f_array)
    print(max_min_in_arr(f_array))
    print("# 6==========================")
    q_array = foo()
    print(q_array)
    print(sum_array(q_array))
    print("# 7==========================")
    ran_arr = fooo()
    print(ran_arr)
    print(min_t_arr(ran_arr))
    print("# 8==========================")
    print(matrix())
    print("# 9==========================")
    print(max_matrix())