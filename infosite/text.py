import psycopg2
import re
import time

import requests
from bs4 import BeautifulSoup

# 通过ip网站获取代理ip
from lxml import etree


def cast_a_vote(url, headers, ip_list):
    for ip in ip_list:
        ip = ip.lower()
        proxies = {ip.split(':')[0]: ip}
        try:
            for i in range(0, 8):
                web_data = requests.get(url, headers=headers, proxies=proxies, timeout=1)
                print(web_data.text)
        except Exception as e:
            continue


def get_ip_port():
    url = 'http://www.ip181.com/'
    a = requests.get(url).text
    # 获取网站所有的代理ip
    # a = '{"ERRORCODE":"0","RESULT":[{"position":"荷兰XXXX XX","port":"6256","ip":"213.75.130.15"},{"position":"欧洲XXXX XX","port":"7207","ip":"152.89.73.217"},{"position":"日本XXXX XX","port":"5111","ip":"126.178.217.175"},{"position":"美国佛罗里达XX XX","port":"2107","ip":"172.109.26.11"},{"position":"美国加利福尼亚XX 阿里云","port":"7516","ip":"11.217.23.105"},{"position":"美国XXXX XX","port":"609","ip":"214.1.104.204"},{"position":"美国XXXX 威瑞森","port":"2089","ip":"72.107.58.21"},{"position":"美国缅因XX XX","port":"4097","ip":"74.78.25.127"},{"position":"摩洛哥XXXX XX","port":"212","ip":"105.158.39.156"},{"position":"波兰XXXX XX","port":"9700","ip":"62.69.219.82"},{"position":"美国XXXX XX","port":"4758","ip":"29.192.209.207"},{"position":"瑞典XXXX XX","port":"6036","ip":"153.112.69.63"},{"position":"澳大利亚XXXX XX","port":"8599","ip":"211.30.137.98"}]}'

    print(a)
    rr = re.compile('port":"(.*?)","ip":"(.*?)"')
    res = rr.findall(a)
    print(res)
    print(type(res))
    # 返回值类型[('7788','47.39.12.1'),]
    return res


# 获取58页面所有租房信息
def spider(url, ip_list):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    # for i in ip_list:
    #     print(i)
    #     ip = i[1]
    #     port = i[0]
    #     print(ip, port)
    #     proxies = {str(ip): str(port)}
    #
    #     web_data = requests.get(url, headers=headers, proxies=proxies, timeout=10)
    #     print(web_data.status_code)
    #     html = web_data.text
    #
    #     print(html)
    #     # time.sleep(1)
    #     return html
    html = " "
    for i in ip_list:
        print(i)
        ip = i[1]
        port = i[0]
        print(ip, port)
        proxies = {str(ip): str(port)}

        web_data = requests.get(url, headers=headers, proxies=proxies, timeout=10)
        print(web_data.status_code)
        html = web_data.text

        print(html)
        # time.sleep(1)
        break
    return html


def get_content_infomation(res, i):


    html = etree.HTML(res)
    # print(html)
    start_url = "http:"
    jjr_img = "none"
    res_jjr_img = html.xpath("//div[@class ='agent-head-portrait pr']/a/img/@src")
    if res_jjr_img:
        jjr_img = start_url + res_jjr_img[0]
    jjr = "none"
    res_jjr = html.xpath("//div/p[@class='agent-name f16 pr']/a/text()")
    if res_jjr:
        jjr = res_jjr[0]

    jjr_phone = "none"
    res_jjr_phone = html.xpath("//div[@class ='house-chat-phone']/span[@class='house-chat-txt']/text()")
    if res_jjr_phone:
        jjr_phone = res_jjr_phone[0]
    print(jjr)
    print(jjr_phone[0])
    month_money = "none"
    try:
        money = html.xpath("//div[@class='house-pay-way f16']/span[@class='c_ff552e']/b/text()")
        # 月租

        month_money = money[0]
        print(month_money)
    except IndexError:
        print("hahahahhhahha")

    info_title = "none"
    title = html.xpath("//div[@class='house-title']/h1[@class='c_333 f20']/text()")
    if title:
        print(info_title)
        info_title = title[0]

    house_mianji = "none"
    mianji = html.xpath("//ul[@class='f14']/li/span/text()")
    if mianji:
        print(mianji[3].split("\xa0\xa0")[1].replace(" ", ""))
        house_mianji = mianji[3].split("\xa0\xa0")[1].replace(" ", "")
    print(house_mianji)

    city_address = "none"
    address ="none"
    res_address = html.xpath("//ul[@class='f14']/li/span/a[@class='c_333 ah']/text()")
    if res_address:
        print(address)
        address = res_address[0]
        city_address = res_address[1]
    print(address)
    print(city_address)
    house_img = "none"
    h_img = html.xpath("//div[@class='basic-top-bigpic pr ']/img[@id='smainPic']/@src")
    if h_img:
        house_img = start_url + h_img[0]
    print(house_img)

    conn = psycopg2.connect(dbname="test2", user="test",
                            password="123456", host="127.0.0.1", port="5432")
    cursor = conn.cursor()
    cursor.execute(
        " UPDATE zufang_zufang_info SET title='%s',month_money='%s',mianji='%s',img='%s',jjr_img='%s',jjr='%s',jjr_phone='%s',address='%s',city_address='%s' WHERE id='%d';" % (
            info_title, month_money, house_mianji, house_img, jjr_img, jjr, jjr_phone, address,city_address,i))
    conn.commit()


def get_web_html(i, proxies):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }

    # "http://zz.58.com/chuzu/?PGTID=0d200001-0015-65b4-0981-4da49d881bed&ClickID=4"
    # 测试使用
    # url="http://zz.58.com/chuzu/?PGTID=0d200001-0015-65b4-0981-4da49d881bed&ClickID=4"

    url = 'http://zz.58.com/chuzu/pn' + str(i)
    web_data = requests.get(url, headers=headers, proxies=proxies, timeout=1)
    print(web_data.status_code)
    html = web_data.text

    get_index_infomation(html)
    time.sleep(1)
    # print(i)


#     连接数据库进行操作
def db_conn(i, title, month_money, mianji, img, next_url):
    i = i + 1
    conn = psycopg2.connect(dbname="test2", user="test",
                            password="123456", host="127.0.0.1", port="5432")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO zufang_zufang_info VALUES('%d','%s', '%s', '%s','%s','%s','none','none','none')" % (
            i, title, month_money, mianji, img, next_url))
    conn.commit()

    # s = "INSERT INTO zufang_zufang_info VALUES('%s', '%s', '%s')"%("dsd","dsds","dffdqq")
    # print(s)
    # rows = cursor.fetchall()


def db_add(title, month_money, mianji, img, jjr_img, jjr, jjr_phone, address):
    conn = psycopg2.connect(dbname="test2", user="test",
                            password="123456", host="127.0.0.1", port="5432")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO zufang_zufang_info VALUES('%s','%s', '%s', '%s','%s')" % (i, title, month_money, mianji, img))
    conn.commit()

    # s = "INSERT INTO zufang_zufang_info VALUES('%s', '%s', '%s')"%("dsd","dsds","dffdqq")
    # print(s)
    # rows = cursor.fetchall()


def get_index_infomation(res):
    html = etree.HTML(res)
    print(html)
    title = html.xpath("//div[@class='des']/h2/a/text()")
    print(len(title), "title")
    # for i in title:
    #     print(i.strip())

    #    租房信息的标题
    money = html.xpath("//div[@class='money']/b/text()")
    # print(money)
    print(len(money), "money")
    #     月租

    mianji = html.xpath("//div/p[@class='room']/text()")
    # for i in mianji:
    #     print(i.split())
    print(len(mianji), "mianji")
    #         面积

    jjr = html.xpath("//span[@class='listjjr']/text()")
    # for i in jjr:
    #     print(i.strip())
    #         经纪人
    address = html.xpath("//div/p[@class='add']/a/text()")
    # print(address)
    # 地址
    img = html.xpath("//div[@class='img_list']/a/img/@lazy_src")
    # 首页imgurl图片地址
    # print(img)

    # for i in img:
    #     img_url = "http://" + i
    #     print(img_url)
    next_url = html.xpath("//div[@class='listBox']/ul/li/@logr")

    start_url = "http://zz.58.com/zufang/"
    ip_list = get_ip_port()
    # 存入数据库
    for i, j in enumerate(money):
        print("++" * 10)
        a = title[i].strip()
        # a是标题
        b = money[i]
        # b是月租
        c = mianji[i].split()[1]
        # c是面积
        # 传给dbconn 存入数据库
        img_url = "http://"
        d = img_url + img[i]
        # d是图片
        content_url = start_url + next_url[i].split("_")[3] + "x.shtml"
        # print(content_url)
        db_conn(i, a, b, c, d, content_url)


#         a就是得到租房信息的详情html


def mian_content_data():
    conn = psycopg2.connect(dbname="test2", user="test",
                            password="123456", host="127.0.0.1", port="5432")
    cursor = conn.cursor()
    cursor.execute(
        "select next_url,id from zufang_zufang_info")
    # conn.commit()
    res = cursor.fetchall()
    for i, j in enumerate(res):
        print(j[0])
        ip_list = get_ip_port()
        html = spider(j[0], ip_list)

        get_content_infomation(html, j[1])

#     数据库去重，删除空数据
def db_delete():
    conn = psycopg2.connect(dbname="test2", user="test",
                            password="123456", host="127.0.0.1", port="5432")
    cursor = conn.cursor()
    cursor.execute(
        "delete from zufang_zufang_info where title='none'")
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # 爬取index内容
    # res_list = get_ip_port()
    # j = 1
    # for i in res_list:
    #     print(i)
    #     ip = i[1]
    #     port = i[0]
    #     print(ip, port)
    #     proxies = {str(ip): str(port)}
    #     get_web_html(j, proxies)
    #     j += 1
    #     break

    mian_content_data()
    # db_delete()


    # dbconn()

    # ip_list = get_ip_list(url, headers=headers)
    # cast_a_vote(vote_url, headers, ip_list)
