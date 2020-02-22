from sys import stdout

if __name__ == '__main__':
    target = int(input('输入四位整数:'))
    list1 = []
    list1.append(target % 10 // 1)  # 个位
    list1.append(target % 100 // 10)
    list1.append(target % 1000 // 100)
    list1.append(target // 1000)

    for i in range(4):
        list1[i] += 5
        list1[i] %= 10
    for i in range(2):
        list1[i], list1[3-i] = list1[3-i], list1[i]
    for i in range(3, -1, -1):
        stdout.write(str(list1[i]))
