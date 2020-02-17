import string
try:
    with open('D:\\python\\test.txt') as f:
        s = f.read()
except IOError:
    print('文件读取失败')


letters = 0
space = 0
digit = 0
others = 0
i= 0
while i < len(s):
    c = s[i]
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
    i += 1

print('char = %d,space = %d,digit = %d,others = %d' % (letters, space, digit, others))