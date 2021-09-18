numb_1 = int(input())                         #ввод числа возводимое в степень
degree = int(input())                         #ввод степени в которую возводится число
degree += 1
numb_2 = 1                                    #создание переменной numb_2 которой будет присваиваться результат вычислений
def func_1():                                 #создание функции func_1
    global numb_2                             #присвоим переменной numb_2 глобальный статус
    if degree>0:
        for i in range(1 , degree):
             numb_2 *=numb_1
        else:
            for i in range (1 , degree*(-1)): #возведение числа в отрицательную степень
                numb_2 *= 1/numb_1            
    return numb_2                             #возращаем значение переменной numb_2
print (func_1())                              #вызываем функцию func_1

