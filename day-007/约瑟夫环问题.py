"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""


def main():
    ary = [x for x in range(0, 15)]  # 基督教徒
    print(ary)
    ary2 = [x for x in range(ord('a'), ord('p'))]
    # print(ary2)
    for index, value in enumerate(ary2):
        ary2[index] = chr(value)

    print(ary2)

    insert_index = 0

    while len(ary2) > 0:
        insert_index += 9
        len_ary = len(ary)
        if insert_index >= len_ary:
            insert_index -= len_ary
        ary.insert(insert_index, ary2[0])
        ary2 = ary2[1:]

    print(ary)


if __name__ == '__main__':
    main()
