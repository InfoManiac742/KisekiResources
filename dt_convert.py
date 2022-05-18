with open('T_ITEM2._DT', 'rb') as f:
    file = f.read()

names = []
descs = []

begin_addr = int.from_bytes(file[0:2],'little')//2

for i in range(begin_addr):
    start = int.from_bytes(file[2*i:2*i+2],'little')
    start += 4
    end = file.find(b'\x00', start)
    string = file[start:end].decode('shift-jis')
    names.append(string)
    start = end+1
    end = file.find(b'\x00', start)
    string = file[start:end].decode('shift-jis')
    descs.append(string)

output = ''
for i in range(begin_addr):
    output += names[i]
    output += '\t'
    output += descs[i]
    output += '\n'

print(output)
