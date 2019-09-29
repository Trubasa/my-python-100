import requests
from bs4 import BeautifulSoup
from time import time


def get_web_dom():
    res = requests.get(
        "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E8%A1%A8%E6%83%85")
    return BeautifulSoup(res.content)


def main():
    dom = get_web_dom()
    imgs = dom.select("img")
    # imgs_url=map(lambda x:x.src,imgs)
    # print(type(imgs))
    # print(imgs)
    for img in imgs:
        url=img.get('src')
        print(url)
        res=requests.get(f'http:{url}')
        if res:
            with open(f'download/{time()}.jpg', 'wb') as f:
                f.write(res.content)


if __name__ == '__main__':
    main()
