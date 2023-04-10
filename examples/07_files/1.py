result = {}
with open(r'C:\Pyneng\pyneng_my_exercises\examples\08_python_basic_examples\sh_ip_int_br.txt') as f:
    for line in f:
        line_list = line.split()
        if line_list and line_list[1][0].isdigit():
            interface = line_list[0]
            ip = line_list[1]
            result[interface] = ip

print(result)
