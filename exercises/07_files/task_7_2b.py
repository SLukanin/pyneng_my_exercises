# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

from sys import argv
from pprint import pprint

config_list = []
with open(argv[1]) as f:
    for line in f:
        #line = line.rstrip()
        not_in_ignore = True
        for i in ignore:
            if i in line:
                not_in_ignore = False        
        if ('!' not in line) and not_in_ignore: #not any(ign in line for ign in ignore):
            config_list.append(line)

with open(argv[2], 'w') as dest:
    dest.writelines(config_list)