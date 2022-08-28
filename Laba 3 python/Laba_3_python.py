
import math

def funct1():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Задание №1: Вычислить и вывести на экран или в файл в виде таблицы значения функции, \nзаданной графически, на интервале от Xнач до Xкон с шагом dx. Интервал и шаг задать таким образом, \nчтобы проверить все ветви программы. Таблица должна иметь заголовок и шапку.\n")
    print("Таблица результатов вычисления значений данного графика функций")
    print("————————————————————————————————————————————————")
    print("№\t|\tX\t\t|\tY")
    print("————————————————————————————————————————————————")
    counter = 0
    
    for x in range(-50, 50+1, 1):
        if ((x/10 <= -2) or (x/10 >= 2)):
            y = (abs(x/10) - 2)/3
        if ((x/10 > -2) and (x/10 < 2) and (x/10 != 0)):
            y = math.log(abs(1 / math.tan(x/10 / 2)))
        counter = counter + 1
        print(str(counter) + ":\t|\tx = " + str(x/10) + "\t|\ty = " + str(y))
        
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def Summary(x, deep):   #Функция для расчета значения y(x)
    global n
    sum = 0
    element = 1
    while abs(element)>=deep:
        sum = sum + element
        k = (4 * n - 5) / (4 * n)
        element = element * k * (-x)
        n = n + 1
    return(sum)

def funct2():   #Задание №2
    global n
    n = 1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Задание №2: Вычислить и вывести на экран в виде таблицы значения функции, \nзаданной с помощью степенного ряда, на интервале от Xнач до Xкон с шагом dx с \nточностью E (вводится пользователем).Таблица должна иметь заголовок и шапку. \nКаждая строка таблицы должна содержать значение аргумента, значение функции и \nколичество просуммированных членов ряда.")
    print()
    deep = 0.0001
    f = int(input("Введите точность определяемого значения:\n: "))
    deep = 1 * pow(10, -f)
    print()
    print("Сравнение результатов вычисления ряда Тейлора для функции (1+x)^(1/4) и результатов функции (1+x)^(1/4)")
    print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
    print("№\t|\tX\t\t|\tКол-во членов ряда\t|\tРяд Тейлора\t|\tОригинальная функция (1+x)^(1/4)")
    print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
    count = 0
    for x in range (1, 10, 1):
        y = Summary(x/10, deep)
        count = count + 1
        f_res = math.pow((1 + x/10),(1 / 4) )
        print( str(count) + "\t|\tx = " + str(x/10) + "\t\t|\tn = " + str(n) + "\t\t\t|\tsum = " + str(toFixed(y,f)) + "\t|\t(1 + " + str(x/10) + ")^(1/4) = " + str( toFixed( f_res,f ) ) )
        n = 1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def funct3():   #Алгоритм Евклида
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Задание №3: Реализовать a^x mod p Сравнения по модулю простого числа через теорему Ферма и свойства сравнений.")
    a = 3   #Основание
    b = 11  #Степень
    p = 5   #Делитель
    print("a^b mod p = " + str(a) + "^" + str(b) + " mod " + str(p) + " = ", end = "")
    b%=(p-1)
    a %= p
    result = 1  #Остаток от деления
    for x in range(1, b+1, 1):
        result *= a
        result %= p
    print(str(result))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def funct4():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Задание №4: Реализовать обобщенный алгоритм Евклида для вычисления с*d mod m=1.")
    b = 262
    a = 22
    rDecrease1 = b
    rZero = a
    r = 0
    q = 0
    while (rZero>0):
        q = rDecrease1 // rZero
        r = rDecrease1 - q * rZero
        rDecrease1 = rZero
        rZero = r
    print("НОД("+str(a)+", "+str(b)+") = "+str(rDecrease1))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def mod(x_a,y_a, z_a):
    for x_a in range(0,z_a):
        if (x_a * y_a) % z_a == 1:
            return x_a
        break
    
def gcd(x,y):
    if (y == 0):
        return x
    else:
        return gcd(y,x%y)

def AlgEv(num,power,mod):
    power = power % (mod - 1)
    num %= mod
    
    result = 1
    for i in range(1, power+1, 1):
        result *= num
        result %= mod
    return result

def encode(str,key):
    temp = key
    keyLen = 0
    while (temp > 0):
        temp /= 10
        keyLen += 1
    i = 0
    t_1 = 0
    e_list = []
    while( i < len(str)):
        t_1 = math.pow(10, i % keyLen)
        e_list.append(((key // t_1) % 10))
        i+=1
    return e_list

def decode(stringInp,key):
    temp = key
    keyLen = 0
    while (temp > 0):
        temp /= 10
        keyLen += 1
    i = 0
    t_1 = 0
    t_2 = 0
    while (i < stringInp.lenght()):
        t1 = pow(10, i % keyLen)
        stringInp[i] -= ((key // t1) % 10) - 1;
        i += 1
    return stringInp;
def funct5():
    X_a = 0
    print("Сейчас вы Алиса\n")
    print("Введите 3 простых числа\n")
    p_a = int(input())
    q_a = int(input())
    Y_a = int(input())
    print("Первые 2 числа- это ваш приватный ключ\n")
    N_a = p_a * q_a
    z = (p_a - 1) * (q_a - 1)
    while gcd(Y_a, z) == 0:
        print("Числа невзаимно простые, введите новое простое число\n")
        Y_a = int(input())
    print("Открытый ключ Алисы(доступен всем)" + "  " + str(N_a) + " и " + str(Y_a))
    print("Теперь вы Боб\nВам нужно закодировать какое-то сообщение и передать его Алисе\n")
    print("Введите ключ (число сдвигов в слове) и само слово:\n")
    key_1 = int(input())
    stringInp = input()
    print("Это ваше зашифрованное слово\n")
    print(encode(stringInp, key_1))
    print("Теперь Боб отправляет зашифрованный сдвиг Алисе : e = " + str(AlgEv(key_1, Y_a, N_a)))
    e = AlgEv(key_1, Y_a, N_a)
    print("Теперь вы Алиса\n" + "Вам пришло зашифрованное письмо от Боба\n" + "Расшифровка прошла успешно\n")
    key_2 = AlgEv(e, mod(X_a, Y_a, z), N_a)
    print(decode(stringInp, key_2))

numberOfFunction = int()
#funct1()
#funct2()
#funct3()
funct5()
