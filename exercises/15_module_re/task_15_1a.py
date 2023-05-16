# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""

import re
from pprint import pprint


def get_ip_from_cfg(file):
    regex = r'ip address *(?P<ip>\S+) *(?P<mask>\S+)|^interface *(?P<intf>\S+)'
    result = {}
    with open(file) as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                if match.lastgroup == 'intf':
                    interface = match.group('intf')
                    result[interface] = []
                else:
                    result[interface] = match.group('ip', 'mask')
    result = {key: value for key, value in result.items() if value}
    return result


if __name__ == '__main__':
    res = get_ip_from_cfg('config_r1.txt')
    pprint(res)
