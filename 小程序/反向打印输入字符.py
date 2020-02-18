string = input('请输入字符串:')
longth = len(string)

def output(s,l):
    if l == 0:
        return
    print(s[l-1])
    output(s, l-1)


def main():
    output(string, longth)


if __name__ == '__main__':
    main()