# zufang_info
这是一个爬取网站租房信息，对数据进行分析并且进行可视化展示的一个项目

现在已经实现了初步的对58郑州租房页面的爬取，和分析
并在web上进行展示。
next step：把爬取到的详情页next_url和下一页的链接分别存到数据库表中，重构爬虫模块代码
step 2：实现分布式爬虫，使用celery+rabbitmq
step 3：用spider实现爬虫功能


7.29  实现next step 和step2 重新设计表 用celery进行爬取
