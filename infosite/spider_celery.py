import psycopg2


# 通过ip网站获取代理ip
from lxml import etree

from text import get_ip_port, spider, get_content_infomation



conn = psycopg2.connect(dbname="test3", user="test",
                        password="123456", host="127.0.0.1", port="5432")
cursor = conn.cursor()
cursor.execute(
    "select next_url,url_id from zufang_zufang_url")
res = cursor.fetchall()
for i, j in enumerate(res):
    print(j[0])
    ip_list = get_ip_port()
    html = spider(j[0], ip_list)
    print("****"*10)
    get_content_infomation.delay(html, j[1])