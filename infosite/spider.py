import random
import time
from bs4 import BeautifulSoup
import requests

from lxml import etree




def getinfomation(url):
    a = ["Mozilla / 5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 66.0.3359.181Safari / 537.36",
         "Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 39.0.2171.71Safari / 537.36",
         "Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 30.0.1599.101Safari / 537.36",
         "Mozilla / 5.0(Windows NT 6.1;WOW64;rv: 34.0) Gecko / 20100101Firefox / 34.0",
         "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2"]
    b = a[random.randint(0, 5)]
    print(b)
    headers = {
        "User-Agent": b

    }
    ip = "122.95.84.98"
    pp_data = "4333"
    new_data = {"http": ip + ":" + pp_data}
    print(new_data)
    res = requests.get(url, headers, proxies=new_data).text
    print(res)
    html = etree.HTML(res)
    print(html)

    title = html.xpath("//div[@class='des']/h2/a/text()")
    print(title)
    for i in title:
        print(i.strip())
    #    租房信息的标题
    money = html.xpath("//div[@class='money']/b/text()")
    print(money)
    #     月租
    mianji = html.xpath("//div/p[@class='room']/text()")
    for i in mianji:
        print(i.split())
    #         面积
    jjr = html.xpath("//span[@class='listjjr']/text()")
    print(jjr)
    for i in jjr:
        print(i.strip())
    #         经纪人
    address = html.xpath("//div/p[@class='add']/a/text()")
    print(address)
# 位置

if __name__ == "__main__":
    # for i in range(1, 10):
    #     url = "http://zz.58.com/chuzu/pn2"
    #     url = url + str(i)
    #     getinfomation(url)
    #     print(url)
    #     time.sleep(5)

    getinfomation("http://zz.58.com/chuzu/pn5")


