import requests

def main():
    res=requests.get("http://www.baidu.com")
    print(res.content)


if __name__ == '__main__':
    main()
