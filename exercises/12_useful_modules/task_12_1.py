# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess
from pprint import pprint

def ping_ip_addresses(ip_list):
    reachable_ip = []
    unreachable_ip = []
    for ip in ip_list:
        result = subprocess.run(
            f"ping {ip}",
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
            )
        if result.returncode == 0:
            reachable_ip.append(ip)
        else:
            unreachable_ip.append(ip)
    

    return (reachable_ip, unreachable_ip)

if __name__ == '__main__':
    ips = [
        '8.8.8.8',
        '172.16.0.1',
        'ya.ru'
    ]
    res = ping_ip_addresses(ips)
    pprint(res)
