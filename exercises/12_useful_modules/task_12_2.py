# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
from pprint import pprint
from task_12_1 import ping_ip_addresses
import ipaddress

def convert_ranges_to_ip_list(ip_list):
    ips = []
    for ip in ip_list:
        if not '-' in ip:
            ips.append(ip)
        else:
            st, end = ip.split('-')
            st_oct = st.split('.')[-1]
            end_oct = end.split('.')[-1]
            oct1, oct2, oct3, oct4 = st.split('.')
            i = int(st_oct)
            while i <= int(end_oct):
                ips.append(f'{oct1}.{oct2}.{oct3}.{str(i)}')
                i += 1
    return ips

if __name__ == '__main__':
    ip_listt = [
        '8.8.8.8',
        '172.16.0.1-3',
        '192.168.88.1'
    ]
    ip_listt = convert_ranges_to_ip_list(ip_listt)
    pprint(ip_listt)
    
    ip = ping_ip_addresses(ip_listt)