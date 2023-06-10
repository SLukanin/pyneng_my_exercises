# -*- coding: utf-8 -*-
"""
Задание 20.5a

Создать функцию configure_vpn, которая использует
шаблоны из задания 20.5 для настройки VPN на маршрутизаторах
на основе данных в словаре data.

Параметры функции:
* src_device_params - словарь с параметрами подключения к устройству 1
* dst_device_params - словарь с параметрами подключения к устройству 2
* src_template - имя файла с шаблоном, который создает конфигурацию для строны 1
* dst_template - имя файла с шаблоном, который создает конфигурацию для строны 2
* vpn_data_dict - словарь со значениями, которые надо подставить в шаблоны

Функция должна настроить VPN на основе шаблонов
и данных на каждом устройстве с помощью netmiko.
Функция возвращает кортеж с выводом команд с двух
маршрутизаторов (вывод, которые возвращает метод netmiko send_config_set).
Первый элемент кортежа - вывод с первого устройства (строка),
второй элемент кортежа - вывод со второго устройства.

При этом, в словаре data не указан номер интерфейса Tunnel,
который надо использовать.
Номер надо определить самостоятельно на основе информации с оборудования.
Если на маршрутизаторе нет интерфейсов Tunnel,
взять номер 0, если есть взять ближайший свободный номер,
но одинаковый для двух маршрутизаторов.

Например, если на маршрутизаторе src такие интерфейсы: Tunnel1, Tunnel4.
А на маршрутизаторе dest такие: Tunnel2, Tunnel3, Tunnel8.
Первый свободный номер одинаковый для двух маршрутизаторов будет 5.
И надо будет настроить интерфейс Tunnel 5.

Для этого задания тест проверяет работу функции на первых двух устройствах
из файла devices.yaml. И проверяет, что в выводе есть команды настройки
интерфейсов, но при этом не проверяет настроенные номера тунелей и другие команды.
Они должны быть, но тест упрощен, чтобы было больше свободы выполнения.
"""
import yaml
from jinja2 import FileSystemLoader, Environment
from netmiko import (ConnectHandler, 
                     NetMikoAuthenticationException,
                     NetmikoTimeoutException)
from task_20_1 import generate_config
import re
from pprint import pprint

data = {
    "tun_num": None,
    "wan_ip_1": "192.168.100.1",
    "wan_ip_2": "192.168.100.2",
    "tun_ip_1": "10.0.1.1 255.255.255.252",
    "tun_ip_2": "10.0.1.2 255.255.255.252",
}

def configure_vpn(src_device_params, 
                  dst_device_params, 
                  src_template, 
                  dst_template, 
                  vpn_data_dict):
    non_free_intfs = []
    src_loopbacks = get_free_interface(src_device_params)
    dst_loopbacks = get_free_interface(dst_device_params)
    non_free_intfs.extend(src_loopbacks)
    non_free_intfs.extend(dst_loopbacks)
    non_free_intfs = list(set(non_free_intfs))
    non_free_intfs.sort()

    free_loopback = 0
    for i in range(20):
        if i not in non_free_intfs:
            free_loopback = i
            break
    vpn_data_dict['tun_num'] = free_loopback
    pprint(vpn_data_dict)

    config_1 = generate_config(src_template, vpn_data_dict).split('\n')
    config_2 = generate_config(dst_template, vpn_data_dict).split('\n')
    
    try:
        with ConnectHandler(**src_device_params) as ssh:
            ssh.enable()
            ssh.send_command("terminal length 0")
            ssh.send_config_set(config_1)
    except (NetMikoAuthenticationException, NetmikoTimeoutException) as error:
        print(error)

    try:
        with ConnectHandler(**dst_device_params) as ssh:
            ssh.enable()
            ssh.send_command("terminal length 0")
            ssh.send_config_set(config_2)
    except (NetMikoAuthenticationException, NetmikoTimeoutException) as error:
        print(error) 
    return

def get_free_interface(device):
    regex = r'Tunnel(\d+)'
    with ConnectHandler(**device) as ssh:
        output = ssh.send_command('show ip int br')
    match = re.finditer(regex, output)
    loopbacks = [int(m.group(1)) for m in match if match]
    return loopbacks


if __name__ == '__main__':
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    
    intfs = get_free_interface(devices[2])
    print(intfs)

    # configure_vpn(devices[1], devices[2],
    #               'templates/gre_ipsec_vpn_1.txt',
    #               'templates/gre_ipsec_vpn_1.txt',
    #                data)