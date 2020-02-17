from sys import stdout  # print会自动换行，stdout可以连续写

for i in range(4):
    for j in range(2 - i + 1):
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    print()
for i in range(3):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(5 - 2 * i):
        stdout.write('*')
    print()