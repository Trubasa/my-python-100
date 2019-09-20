"""
判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数
"""


def main():
    my_input = input("请输入")

    def is_palindrome(num_str):
        middle = len(num_str) // 2
        is_yes = True
        for index in range(0, middle):
            if (num_str[index]) != num_str[-(index + 1)]:
                is_yes = False
                break
        print('结果：%s' % ('是' if is_yes else "不是"))
    is_palindrome(my_input)
    main()


if __name__ == '__main__':
    main()
