def main():
    f = None
    try:
        f = open("hell.txt", 'r', encoding="utf-8")
    except:
        print("err")
    print(f.read())
    f.close()


if __name__ == '__main__':
    main()
