"""
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只
"""

def main():
    for a in range(0, 100):
        for b in range(0, 100):
            c = 100 - a - b
            if a * 5 + b * 3 + c / 3 == 100:
                print("a:%d ,b:%d,c:%d" % (a, b, c))


main()