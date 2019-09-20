"""
输出2~99之间的素数
"""
import math


def main():
    def is_prime(num):
        if num==1:
            return True
        elif num==2:
            return True

        is_yes = True
        for i in range(2, int(math.sqrt(num)) + 1):
            # print(num, i, num % i)
            if num % i == 0:
                is_yes = False
                break
        return is_yes

    for i in range(2, 100):
        if is_prime(i):
            print(i,end=" ")


if __name__ == '__main__':
    main()
