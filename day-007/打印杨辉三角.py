def main():
    num = int(input('input num '))

    def return_ary(num):
        if num == 1:
            return [[1]]
        elif num == 2:
            return [[1], [1, 1]]
        else:
            pre_ary = return_ary(num - 1)
            pre_row = pre_ary[-1]
            cur_row = []
            cur_row.append(1)
            for i in range(0, len(pre_row)-1):
                cur_row.append(pre_row[i] + pre_row[i + 1])
            cur_row.append(1)
            new_ary = pre_ary[:]
            new_ary.append(cur_row)
            return new_ary


    for ele in return_ary(num):
        print(ele)


if __name__ == '__main__':
    while True:
        main()
