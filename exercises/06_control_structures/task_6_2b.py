# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_type = ""
error = 'Неправильный IP-адрес'
error_flag = False

while not error_flag:

    ip = input('Введите IP в формате 10.0.1.1: ')

    ip_list = ip.split('.')
    if len(ip_list) != 4:
        error_flag = True
    else:
        for i in ip_list:
            if not (int(i.isdigit()) and (0 <= int(i) <= 255)):
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
        error_flag = True
    else:
        print(error)
        error_flag = False
        continue
