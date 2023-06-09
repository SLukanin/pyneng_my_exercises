# -*- coding: utf-8 -*-
"""
Задание 18.2a

Скопировать функцию send_config_commands из задания 18.2 и добавить параметр log,
который контролирует будет ли выводится на стандартный поток вывода информация о том
к какому устройству выполняется подключение.
По умолчанию, результат должен выводиться.

Пример работы функции:

In [13]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...

In [14]: result = send_config_commands(r1, commands, log=False)

In [15]:

Скрипт должен отправлять список команд commands на все устройства
из файла devices.yaml с помощью функции send_config_commands.
"""
from netmiko import (ConnectHandler,
                     NetMikoAuthenticationException,
                      NetMikoTimeoutException )
from netmiko.ssh_exception import SSHException
import yaml

def send_config_commands(device, config_commands, log = True):
    result = ''
    try:
        with ConnectHandler(**device) as ssh:
            if log:
                print('подключаюсь к {}...'.format(device['host']))
            ssh.enable()
            result = ssh.send_config_set(config_commands)
    except(NetMikoAuthenticationException, SSHException, NetMikoTimeoutException) as error:
        print(error)

    return result



if __name__ == '__main__':
    commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
    output = ''
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
        for device in devices:
            output += send_config_commands(device, commands)
            
    print(output)