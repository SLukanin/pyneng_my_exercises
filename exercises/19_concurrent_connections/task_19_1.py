# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
import subprocess

ip_list = ['192.168.88.1', 
           '8.8.8.8', 
           'ya.ru',
           '10.10.10.10']

def ping_ip(ip):
    result = subprocess.run(['ping', '-c', '3', ip], stdout=subprocess.PIPE)
    return result

def ping_ip_addresses(ip_list, limit=3):
    reachable_ip = []
    unreachable_ip = []

    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(ping_ip, ip_list)
        # for ip, res_code in zip(ip_list, result):
        #     print(f'{ip}  : результат пинга {res_code.returncode}')
        for status, ip in zip(result, ip_list):
            if status.returncode == 0:
                reachable_ip.append(ip)
            else:
                unreachable_ip.append(ip)
    return reachable_ip, unreachable_ip

if __name__ == '__main__':
    pprint(ping_ip_addresses(ip_list, limit=3))




