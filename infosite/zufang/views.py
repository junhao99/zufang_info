from django.shortcuts import render

# Create your views here.
from zufang.models import Zufang_Info


def show_main_info(response):
    # s = Zufang_Info(title = "1",month_money = "100",mianji = "100")

    return render(response, "info_content.html")


def show_info(response):
    s = Zufang_Info.objects.get(id=2)
    # print(s.title, s.month_money)
    dict1 = {}

    res = Zufang_Info.objects.all()
    dict1["aaa"] =res
    # for i in res:
    #     dict1[i.id] = i
    return render(response, "index.html", dict1)
