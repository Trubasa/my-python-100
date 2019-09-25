from random import randint
from time import time, sleep
from os import getpid

def download_task(filename):
    print('[进程%d]开始下载%s...' % (getpid(),filename))
    time_to_download = randint(1, 3)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    print(f"进程{getpid()}")
    start = time()
    download_task('Python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()