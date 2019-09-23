def main():
    ary_str = input('please input')
    ary = ary_str.split(' ')
    the_min = the_max = int(ary[0])
    for ele in ary:
        ele=int(ele)
        if ele > the_max:
            the_max = ele
        if ele < the_min:
            the_min = ele
    print(f"最小值为：{the_min}，最大值为{the_max}")


if __name__ == '__main__':
    while True:
        main()
