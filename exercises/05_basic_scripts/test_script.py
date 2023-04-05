from sys import argv

interface = argv[1]
vlan = argv[2]
protocol = input('твой любимый протокол маршрутизации? ')

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print('протокол: {}'.format(protocol))
print('\n' + '-' * 40  + '\n')
print('interface {} \n'.format(interface))
print('\n'.join(access_template).format(vlan), '\n')

input('press Enter to exit')