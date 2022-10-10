# Задайте натуральное число N.
#  Напишите программу, которая 
#  составит список простых множителей числа N.
number = int(input("Введите число: "))
i = 2
list = []
older = number
while i <= number:
    if number % i == 0:
        list.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {older} : {list}")