my_list = []
my_list2 = []
for i in range(1,15):
    if i % 2 == 0:
        my_list.append(i)

for item in my_list:
    item = item * 2
    my_list2.append(item)

print(my_list)
print(my_list2)

list1 = [i for i in range(20)]
list2= (i for i in range(20))
print(list1,list2)