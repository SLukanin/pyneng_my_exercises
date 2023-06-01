import telnetlib
import time
from pprint import pprint
connection = telnetlib.Telnet('172.16.0.43', 32770)
# connection.read_until(b'>')
# connection.write(b'\r')
#
# connection.expect([b'[>#]', b''])
connection.write(b'\r\n')
print('1: ______________')
connection.write(b'sh ip int brief\r\n')
print('2: ______________')
pprint(connection.expect([b'[>#]'])[2].decode('utf-8'))
time.sleep(5)


connection.write(b'sh arp\r\n')
# connection.write(b'\r\n')
# connection.write(b'\n\r')
print('3: ______________')
pprint(connection.expect([b'[>#]'])[2].decode('utf-8'))
# connection.write(b'\n\r')
print('4: ______________')
pprint(connection.expect([b'[>#]', b' --More--'])[2].decode('utf-8'))
# output = connection.read_until(b'#').decode('utf-8')
# pprint(output)
# connection.write(b'exit\n')
connection.close()
connection.close()
