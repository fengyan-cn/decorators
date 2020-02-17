a = int(input('输入你要分解的数:'))
list1 = []
def resolve(x):
    for i in range(2,x):
        if x % i == 0:
            list1.append(i)
            x = int(x/i)
            return resolve(x)
    else:
        list1.append(x)
    for j in range(len(list1)):
        if j < len(list1)-1:
            print(list1[j],end='*')
        else:
            print(list1[len(list1)-1])

resolve(a)


