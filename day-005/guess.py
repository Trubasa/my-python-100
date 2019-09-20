"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
from random import randint


def main():
    random_num = randint(0, 100)
    while (True):
        my_num = int(input("请输入:"))
        if my_num < random_num:
            print('小了')
        elif my_num > random_num:
            print("大了")
        else:
            print("对了")
            break


if __name__ == '__main__':
    main()
