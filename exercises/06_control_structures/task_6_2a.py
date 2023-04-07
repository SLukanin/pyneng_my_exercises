# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_type = ""
error = 'Неправильный IP-адрес'
error_flag = False
ip = input('Введите IP в формате 10.0.1.1: ')

ip_list_int = []

ip_list = ip.split('.')
if len(ip_list) != 4:
   error_flag = True

for i in ip_list:
   if int(i.isdigit()) and (0 <= int(i) <= 255):
      ip_list_int.append(int(i))
   else:
      error_flag = True
      break

if not error_flag:
   first_octet = int(ip.split('.')[0])
   if ip == '0.0.0.0':
      ip_type = 'unassigned'
   elif ip == '255.255.255.255':
      ip_type = 'local broadcast'
   elif first_octet >= 1 and first_octet <=223:
      ip_type = 'unicast'
   elif 224 <= first_octet <= 239:
      ip_type = 'multicast'
   else:
      ip_type = 'unused'
   print(ip_type)
else:
   print(error)


