# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""

import re
from pprint import pprint


def convert_ios_nat_to_asa(ios_nat, asa_nat):
    config = []
    asa_template = """
object network LOCAL_{ip}
 host {ip}
 nat (inside,outside) static interface service tcp {port1} {port2}"""

    regex = r".+(?P<protocol>tcp|udp) +" \
            r"(?P<ip>[\d.]+) +" \
            r"(?P<port1>\d+) +\w+ +" \
            r"(?P<interface>\S+) +" \
            r"(?P<port2>\d+)"
    with open(ios_nat) as f, open(asa_nat, 'w') as dest:
        config = [m.groupdict() for m in re.finditer(regex, f.read())]
        for dict in config:
            dest.write(asa_template.format(ip=dict['ip'], port1=dict['port1'], port2=dict['port2']))
    pprint(config)
    return


if __name__ == '__main__':
    convert_ios_nat_to_asa('cisco_nat_config.txt', 'asa_nat_config.txt')
