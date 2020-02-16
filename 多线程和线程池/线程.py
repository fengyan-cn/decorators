import time
import threading

class Mythread(threading.Thread):
    #创建了一个线程类并且继承了threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("开始线程:" + self.name)
        moyu_time(self.name, self.counter, 10)
        print('退出线程:' + self.name)


def moyu_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print('%s 开始摸鱼 %s' %(threadName, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        counter -= 1


thread1 = Mythread(1, '小红', 1)
thread2 = Mythread(2, '小明', 2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('退出主线程')