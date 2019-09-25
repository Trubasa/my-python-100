def main():
    try:
        with open('bg.jpg', 'rb') as f:
            data = f.read()
        with open("bg_copy.jpg", "wb") as f2:
            f2.write(data)
    except:
        print("读取文件或者写文件出现问题")


if __name__ == '__main__':
    main()


