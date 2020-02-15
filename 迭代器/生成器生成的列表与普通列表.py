import time
#计算过程时间（end-start） 装饰器实现
def log_func_time(func):
    def wrapper():
        start_time = time.perf_counter()
        my_func = func()
        end_time = time.perf_counter()
        print('方法{}消耗了{}ms'.format(func.__name__,(end_time - start_time) + 1000))
        return my_func
    return wrapper
#列表生成的列表是固定的
@log_func_time
def calc_func_1():
    list1 = [i for i in range(666666)]
#生成器按照一定算法边运行边计算，按照要求计算
@log_func_time
def calc_func_2():
    list2 = (i for i in range(666666))

calc_func_1()
calc_func_2()