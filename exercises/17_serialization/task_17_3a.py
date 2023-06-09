# -*- coding: utf-8 -*-
"""
Задание 17.3a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод
команды show cdp neighbor из нескольких файлов и записывает итоговую
топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами,
независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь
в файл topology.yaml. Он понадобится в следующем задании.

"""
import re
from pprint import pprint
import yaml


def generate_topology_from_cdp(list_of_files, save_to_filename=None):
    regex = r'(?P<dev>\w+) +' \
            r'(?P<l_intf>\S+ \S+) +\d+ [\w ]+ +\S+ +' \
            r'(?P<r_intf>\S+ \S+)'
    topology_dict = {}
    for file in list_of_files:
        with open(file) as f:
            hostname = re.search(r'(\S+)[>#]', f.read()).group(1)
            topology_dict[hostname] = {}
            f.seek(0)
            for line in f.read().split('\n'):
                m = re.search(regex, line)
                if m:
                    l_intf = m.group('l_intf')
                    r_dev = m.group('dev')
                    r_intf = m.group('r_intf')
                    topology_dict[hostname][l_intf] = {r_dev: r_intf}

    if save_to_filename:
        with open(save_to_filename, 'w') as f:
            yaml.dump(topology_dict, f)
    return topology_dict


if __name__ == '__main__':
    list_of_files = ['sh_cdp_n_sw1.txt',
                     'sh_cdp_n_r1.txt',
                     'sh_cdp_n_r2.txt',
                     'sh_cdp_n_r3.txt',
                     'sh_cdp_n_r4.txt',
                     'sh_cdp_n_r5.txt',
                     'sh_cdp_n_r6.txt']
    pprint(generate_topology_from_cdp(list_of_files, save_to_filename='topol.yaml'))
