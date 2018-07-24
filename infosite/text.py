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
def get_webdata(i, proxies):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }

    # for j in range(4, 8):
    url = 'http://zz.58.com/chuzu/pn' + str(i)
    web_data = requests.get(url, headers=headers, proxies=proxies, timeout=1)
    print(web_data.status_code)
    html = web_data.text

    getinfomation(html)
    time.sleep(2)
    # print(i)
def dbconn(i,title,month_money,mianji):
    i = i+1
    conn = psycopg2.connect(dbname="test2", user="test",
                            password="123456", host="127.0.0.1", port="5432")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO zufang_zufang_info VALUES('%d','%s', '%s', '%s')"%(i,title,month_money,mianji))
    conn.commit()
    # s = "INSERT INTO zufang_zufang_info VALUES('%s', '%s', '%s')"%("dsd","dsds","dffdqq")
    # print(s)
    # rows = cursor.fetchall()


def getinfomation(res):
    html = etree.HTML(res)
    print(html)
    title = html.xpath("//div[@class='des']/h2/a/text()")
    print(len(title),"title")
    # for i in title:
    #     print(i.strip())


    #    租房信息的标题
    money = html.xpath("//div[@class='money']/b/text()")
    # print(money)
    print(len(money),"money")
    #     月租

    mianji = html.xpath("//div/p[@class='room']/text()")
    # for i in mianji:
    #     print(i.split())
    print(len(mianji),"mianji")
    #         面积

    jjr = html.xpath("//span[@class='listjjr']/text()")
    # for i in jjr:
    #     print(i.strip())
    #         经纪人
    address = html.xpath("//div/p[@class='add']/a/text()")
    # print(address)
    # 地址

    for i,j in enumerate(money):
        print("++"*10)
        a = title[i].strip()
        # a是标题
        b = money[i]
        # b是月租
        c= mianji[i].split()[1]
        # c是面积
        # 传给dbconn 存入数据库
        dbconn(i,a,b,c)

# 位置
#     info = Zufang_Info.objects.create(title='zhangsan', month_money='male')

if __name__ == '__main__':

    res_list = get_ip_port()
    j = 1
    for i in res_list:
        print(i)
        ip = i[1]
        port = i[0]
        print(ip, port)
        proxies = {str(ip): str(port)}
        get_webdata(j, proxies)
        j += 1


        # try:
        #
        #     get_webdata(j, proxies)
        #     j += 1
        #     break
        # except Exception as e:
        #     print("error")
        #     continue
        # break

    # dbconn()

        # ip_list = get_ip_list(url, headers=headers)
        # cast_a_vote(vote_url, headers, ip_list)
