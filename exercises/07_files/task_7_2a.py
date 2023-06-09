# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]


from sys import argv
from pprint import pprint

config_list = []
with open(argv[1]) as f:
    for line in f:
        line = line.rstrip()
        not_in_ignore = True
        for i in ignore:
            if i in line:
                not_in_ignore = False        
        if ('!' not in line) and not_in_ignore: #not any(ign in line for ign in ignore):
            config_list.append(line)

for line in config_list:
    print(line)