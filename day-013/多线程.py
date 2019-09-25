
from multiprocessing import Process
from random import randint
from time import time, sleep
from os import getpid

def download_task(filename):
    print('[进程%d]开始下载%s...' % (getpid(),filename))
    time_to_download = randint(1, 3)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    print(f'[进程{getpid()}]')
    task_1=Process(target=download_task,args=("奥特曼大战葫芦娃.mkv",))
    task_2=Process(target=download_task,args=("奥特曼大战葫芦娃2.mkv",))
    task_1.start()
    task_2.start()
    task_1.join()
    task_2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))



if __name__ == '__main__':
    main()