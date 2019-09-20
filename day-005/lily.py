"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3
"""


def main():
    for num in range(100, 999):
        total = 0
        for single in str(num):
            total += int(single) ** 3

        if total == int(num):
            print(num, end=" ")


if __name__ == '__main__':
    main()
