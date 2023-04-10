result = {}

with open('sh_ip_interface.txt') as f:
    for line in f:
        if 'line protocol' in line:
            interface = line.split()[0]
        elif 'MTU' in line:
            mtu = line.split()[2]
            result[interface] = mtu

for key, item in result.items():
    print('{:12} : {}'.format(key, item))
