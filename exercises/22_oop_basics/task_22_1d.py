# -*- coding: utf-8 -*-

"""
Задание 22.1d

Изменить класс Topology из задания 22.1c

Добавить метод add_link, который добавляет указанное соединение, если его еще
 нет в топологии.
Если соединение существует, вывести сообщение "Такое соединение существует",
Если одна из сторон есть в топологии, вывести сообщение
"Соединение с одним из портов существует"


Создание топологии
In [7]: t = Topology(topology_example)

In [8]: t.topology
Out[8]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [9]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [11]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
Такое соединение существует

In [12]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
Соединение с одним из портов существует


"""
from pprint import pprint
class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, top_dict):
        unique_dict = {}
        for key, value in top_dict.items():
            if not unique_dict.get(value) == key:
                unique_dict[key] = value
        return unique_dict

    def delete_link(self, point_1, point_2):
        if self.topology.get(point_1) == point_2:
            del self.topology[point_1]
        if self.topology.get(point_2) == point_1:
            del self.topology[point_2]

    def delete_node(self, node):
        copy_dict = self.topology.copy()
        for key, value in copy_dict.items():
            if key[0] == node or value[0]== node:
                del self.topology[key]

    def add_link(self, point_1, point_2):
        is_it_present =False
        for key, value in self.topology.items():
            if (key == point_1 and value == point_2) or (key == point_2 and value == point_1):
                print('Такое соединение существует')
                is_it_present = True
            elif key == point_1 or key == point_2 or value == point_1 or value == point_2:
                print('Соединение с одним из портов существует')
                is_it_present = True
        if not is_it_present:
            self.topology[point_1] = point_2


topology_example = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
}

if __name__ == '__main__':
    top = Topology(topology_example)
    pprint(top.topology)
    print('*' * 50)
    top.add_link(('CRT1', 'GE0/3'),('CSW2', 'GE1/24'))
    pprint(top.topology)
    print('*' * 50)
    top.add_link(("SW1", "Eth0/1"),("R1", "Eth0/0"))
    top.add_link(("R1", "Eth0/0"),("CSW1", "Eth0/1"))
    pprint(top.topology)