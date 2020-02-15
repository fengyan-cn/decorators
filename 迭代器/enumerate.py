#可以将可迭代对象转换为enumerate对象，在统计数据和数字的对应关系的时候可以使用

list1 = ['zhou','hong','ye']
for i in enumerate(list1):
    print(i)

a = list(enumerate(list1))
print(a)

month = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']

for num,value in enumerate(month,1):
    print('{}月 ----> {}'.format(num,value))
