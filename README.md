# Лабораторная работа №4 и №5

## Написание Unit тестов / Знакомство с CI/CD

Данный проект содержит программу, содеражащую некоторые математические и бинарные оперции. Каждая функция содержит подробное описание к применению.

## Список функций:

* **square(n)** - возвращает квадрат числа n.

|Input  |Output|
|-------|------|
|n (int/float)|- (int/float)|

Пример вызова:

```
print(square(3))
	#Output: 9
print(square(1.2))
	#Output: 1.44
print(square(-2))
	#Output: 4
```

* **add_binary(a,b)** - возвращает сумму двух чисел в двоичном формате.

|Input  |Output|
|-------|------|
|a (uint)|binary_sum (str)|
|b (uint)|

Пример вызова:

```
print(add_binary(2,5))
	#Output: 111
print(add_binary(9,4))
	#Output: 1101
```

* **sqrt(number, n)** - возвращает корень n-степени числа number.

|Input  |Output|
|-------|------|
|number (uint)|- (float)|
|n (uint)

Пример вызова:

```
print(sqrt(4,2))
	#Output: 2.0
print(sqrt(27,3))
	#Output: 3.0
print(sqrt(5,2))
	#Output: 2.23606797749979
```

## Тесты

Проект содержит 14 тестов на вхождения аругментов в виде целых чисел, нуля, чисел с плавающей точкой и отрицательных чисел для каждой функции.

## История изменения проекта

|Номер коммита|Дата|Автор|Описание|Хэш|
|-------------|----|-----|--------|---|
|1|Декабрь 24|Tigguzrin <grikuzmin777@gmail.com>|Добавлен файл operations.py|add20063e12eba66b668b18ef56e49dac58c46d9|
|2|Декабрь 24|Tigguzrin <grikuzmin777@gmail.com>|Добвлены тесты в operations.py|e7e2f4f2a40feff6db979f552950d2c3359bd60c|
|3|Декабрь 25|Tigguzrin <grikuzmin777@gmail.com>|Создан README.md|af2fc721f764873046790dd62af5fb9c4f464b60|
|4|Декабрь 25|Tigguzrin <grikuzmin777@gmail.com>|Удалены тесты из operations.py|8af7029c8398eb668e0f64297e556ecca40f3910|
|5|Декабрь 25|Tigguzrin <grikuzmin777@gmail.com>|Перенесены тесты в созданный файл tests.py|9c76618a1f6786c7a6b48ab9bb0ae07559f61742|
|6|Декабрь 25|Tigguzrin <grikuzmin777@gmail.com>|Обновлён operations.py. Все тесты успешны|70203d17f5252e7eafd53127d1e7dcffe75fe7f1|
