# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Введтите IP в формате 10.0.1.1: ')
ip_type = ""
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