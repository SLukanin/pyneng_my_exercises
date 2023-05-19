import pexpect
import re
from pprint import pprint

ssh = pexpect.spawn('ssh cisco@192.168.100.1')
ssh.expect('[Pp]assword')
ssh.sendline('cisco')
ssh.expect('[>#]')
ssh.sendline('enable')
ssh.expect('[Pp]assword')
ssh.sendline('cisco')
ssh.expect('[>#]')
ssh.sendline('sh ip int br')
ssh.expect('#')
output = str(ssh.before, encoding='utf-8')
regex1 = r'(?P<intf>\S+) +(?P<ip>\S+) +\w+ +\w+ +(?P<status>up|down|administratively down) +(?P<protocol>up|down)'
regex2 = r'(?P<intf>\S+) +(?P<ip>\S+) +\w+ +\w+ +(?P<status>up|down|administratively down) +(?P<protocol>up|down)'
match = re.finditer(regex1, output)
inft_dict = {}
for m in match:
    inft_dict[m.group('intf')] = {
        'ip': m.group('ip'),
        'status': m.group('status'),
        'protocol': m.group('protocol')
    }
pprint(inft_dict)



