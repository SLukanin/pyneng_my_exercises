# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
n_vlan = int(input('Введите номер VLAN: '))
mac_address_table = []
with open(r'C:\Pyneng\pyneng_my_exercises\exercises\07_files\CAM_table.txt') as f:
    for line in f:
        line_list = line.split()
        if line_list and line_list[0].isdigit():
            line_list[0] = int(line_list[0])
            mac_address_table.append(line_list)
            

mac_address_table.sort()
for vlan, mac, _, intf in mac_address_table:
    if vlan == n_vlan:
        print('{:<9}{:20}{}'.format(vlan, mac, intf))


# for i in mac_address_table:
#     vlan, mac_address, _, intf = i
#     print('{:<9}{:20}{}'.format(vlan, mac_address, intf))