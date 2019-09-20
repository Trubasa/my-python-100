"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
"""


def main():
    def find_factor(number):
        ary = []
        for num in range(1, number-1):
            if number % num == 0:
                ary.append(num)
        # print(number, ary,sum(ary))
        return ary

    for number in range(1, 10000):

        # print(number, sum(find_factor(number)))

        if sum(find_factor(number)) == number:
            print(number, end=" ")


if __name__ == '__main__':
    main()
