import unittest
from decimal import Decimal

def square(n):
    '''Принимает число n, возвращает квадрат числа n

            Параметры:
                    n (int/float): число

            Возвращаемое значение:
                    - (int/float): квадрат числа
    '''
    return float(Decimal(str(n))**2)

def add_binary(a,b):
    '''
    Возвращает сумму двух десятичных чисел в двоичном формате.

            Параметры:
                    a (uint): первое десятичное целое число
                    b (uint): второе десятичное целое число

            Возвращаемое значение:
                    binary_sum (str): двочиная строка a и b
    '''
    if a+b>=0:
        binary_sum = bin(a+b)[2:]
    else:
        binary_sum = '-'+bin(a+b)[3:]
    return binary_sum

def sqrt(number, n):
    '''Принимает число number и степень n, возвращает корень n-ой степени числа number

            Параметры:
                    number (uint): число
                    n (uint): показатель корня

            Возвращаемое значение:
                    - (float): корень числа n-ой степени
    '''
    if number<0:
        raise ValueError("Аргумент корня не может быть отрицательным!")
    return number**(1/n)
