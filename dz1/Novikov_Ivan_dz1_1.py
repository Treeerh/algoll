import random
# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
def sum_product(number):
    s=0; p=1
    for i in number:
        s=s+int(i)
        p=p*int(i)
    return F"Сумма = {s} , Преизведение = {p}"

# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
#     Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
#     Объяснить полученный результат.

def log_arg(a,b):
    a=int(a)
    b=int(b)
    print(a, bin(a))
    print(b, bin(b))
    print("%d & %d = %d (%s)" % (a,b,a&b,bin(a&b)))
    print("%d | %d = %d (%s)" % (a,b,a|b,bin(a|b)))
    print("%d ^ %d = %d (%s)" % (a,b,a^b,bin(a^b)))
    print("%d << 2 = %d (%s)" % (a,a<<2,bin(a<<2)))
    print("%d >> 2 = %d (%s)" % (a,a>>2,bin(a>>2)))

# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b,
#     проходящей через эти точки.
def straight(x1,y1,x2,y2):
    k = (y1-y2) / (x1-x2)
    b = y2 - k * x2
    return F"y = {k} * x + {b}"

# 4. Написать программу, которая генерирует в указанных пользователем границах:
#     случайное целое число;
#     случайное вещественное число;
#     случайный символ.
#     Для каждого из трех случаев пользователь задает свои границы диапазона.
#     Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
#     Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
def random_sif(a,x,y):
    c=''
    b = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z')
    if a == '1':
        c=random.randint(int(x),int(y))
    elif a == '2':
        c=random.uniform(float(x), float(y))
    elif a == '3':
        r_str = random.randint(b.index(x),b.index(y))
        c=b[r_str]
    return c

# 5. Пользователь вводит две буквы. Определить,
#     на каких местах алфавита они стоят и сколько между ними находится букв.
def letter_num(x,y):
    a=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    if x and y in a:
        s = abs(a.index(x) - a.index(y))
    return F"Символ {x} на {a.index(x)}, символ {y} на {a.index(y)}, между ними {s-1} символов"

# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
def letter(nummber):
    c=''
    a=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    if nummber < 26:
        c=a[nummber]
    else:
        nummber = nummber % 26
        c=a[nummber]
    return c

# 7. По длинам трех отрезков, введенных пользователем,
#     определить возможность существования треугольника, составленного из этих отрезков.
#     Если такой треугольник существует, то определить, является ли он разносторонним,
#     равнобедренным или равносторонним
def triangl(len_a,len_b,len_c):
    c=''
    if len_a+len_b>len_c and len_a+len_c>len_b and len_b+len_c>len_a:
        if len_a==len_b==len_c:
            c="равносторонним"
        elif len_a==len_b or len_a==len_c or len_b==len_c:
            c="равнобедренным"
        else:
            c="разносторонним"
    else:
        c="не треугольник"
    return c
# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
def years(num_year):
    c=''
    if (num_year % 4 == 0) and (num_year % 100 != 0) or (num_year % 400 == 0):
        c="YES"
    else:
        c='NO'
    return c

# 9. Вводятся три разных числа. Найти, какое из них является средним
#     (больше одного, но меньше другого).
def average(a,b,c):
    d=''
    if c > a > b or b > a > c:
        d=F"Среднее a = {a}"
    elif c > b > a or a > b > c:
        d=F"Среднее b = {b}"
    else:
        d=F"Среднее c = {c}"
    return d




if __name__== '__main__':
    print("# 1==========================")
    num=input('Введите число = ')
    print(sum_product(num))

    print("# 2==========================")
    a = input('Введите число A =')
    b = input('Введите число B =')
    print(log_arg(a, b))

    print("# 3==========================")
    x1 = float(input('Введите координату А x = '))
    y1 = float(input('Введите координату А y = '))
    x2 = float(input('Введите координату B x = '))
    y2 = float(input('Введите координату B y = '))
    print(straight(x1,y1,x2,y2))

    print("# 4==========================")
    a = input("Введите 1 int, 2 float, 3 str ")
    x = input('введите первый')
    y = input('введите второй')
    print(random_sif(a, x, y))

    print("# 5==========================")
    a=input('Введите символ A =')
    b=input('Введите символ B =')
    print(letter_num(a,b))

    print("# 6==========================")
    a = int(input('Введите номер буквы = '))
    print(letter(a))

    print("# 7==========================")
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    print(triangl(a, b, c))

    print("# 8==========================")
    years_n=int(input('Введите год = '))
    print(years(years_n))

    print("# 9==========================")
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    print(average(a,b,c))
