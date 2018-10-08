
__author__='Алферьев Дмитрий Александрович'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

#def my_round(number, ndigits):
#    pass
#my_round(2.1234567, 5)

def my_round(number, ndigits): 
    number = number*(10**ndigits)+0.41 
    number = number//1 
    return number/(10**ndigits) 
print(my_round(2.1234567, 5)) 



# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

#def lucky_ticket(ticket_number):
#    pass

def lucky_ticket(ticket_number):
    if (len(str(ticket_number))!= 6) or (type(ticket_number) is not int):
        return 'Некорректный номер билета'
    else:
        ticket_number1 = list(str(ticket_number))
        sum1 = int(ticket_number1[0]) + int(ticket_number1[1]) + int(ticket_number1[2])
        sum2 = int(ticket_number1[3]) + int(ticket_number1[4]) + int(ticket_number1[5])
        if sum1 == sum2:
            return 'Билет %s счастливый' %ticket_number
        else:
            return 'Билет %s несчастливый' %ticket_number

#number = int(input('Введите номер билета:'))
number = 123456
print(lucky_ticket(number))
