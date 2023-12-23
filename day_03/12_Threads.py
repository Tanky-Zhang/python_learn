# 进程和线程学习
import multiprocessing
from multiprocessing import Process, Queue
from os import getpid
from random import randint
from time import sleep, time


# 下载任务
def download_task(filename):
    print('启动下载进程，进程号[%d]' % getpid())
    print('开始下载%s......' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成了！耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf',))
    p1.start()
    p2 = Process(target=download_task, args=('Python从入门到住院.pdf',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒' % (end - start))


# if __name__ == '__main__':
#     main()

print('--------------------------------------------------------------------------------------------')

queue = multiprocessing.Queue()


def sub_task(string):
    # print(queue.get())
    # if not q.empty():
    #     counter
    counter = queue.get()
    while counter < 10:
        print(string, end='', flush=True)
        # queue.put(queue.get() + 1)
        counter += 1
        queue.put(counter)
        sleep(0.01)


def main2():
    queue.put(0)
    # print(queue.get())
    Process(target=sub_task, args=('Ping',)).start()
    Process(target=sub_task, args=('Pong',)).start()


# if __name__ == '__main__':
#     # queue.put(1)
#     # print(queue.get())
#     # print(queue.get())
#     main2()

print('--------------------------------------------------------------------------------------------')

from threading import Thread


def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main3():
    start = time()
    t1 = Thread(target=download, args=('Python从入门到住院.pdf',))
    t1.start()
    t2 = Thread(target=download, args=('Peking Hot.avi',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))


if __name__ == '__main__':
    main3()
