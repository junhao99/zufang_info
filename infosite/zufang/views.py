from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import request
from django.shortcuts import render

# Create your views here.
from zufang.models import Zufang_Info


def show_main_info(request):
    # s = Zufang_Info(title = "1",month_money = "100",mianji = "100")

    return render(request, "info_content.html")


def show_info(request):
    contact_list = Zufang_Info.objects.all()
    page_number = Paginator(contact_list, 10)  # Show 25 contacts per page
    print(page_number.num_pages)

    s = Zufang_Info.objects.get(id=2)
    # print(s.title, s.month_money)
    dict1 = {}

    res = Zufang_Info.objects.all()
    dict1["aaa"] = res


    return render(request, "index.html", dict1)


def page(request,one_page):
    print("page")
    print(one_page)
    contact_list = Zufang_Info.objects.all()
    page_number = Paginator(contact_list, 10)  # Show 10 contacts per page
    print(page_number.num_pages)
    print(111)
    contacts = page_number.page(one_page)
    if request.GET.get('page'):
        print("555555555555555")
        try:
            p = request.GET.get('page')
            contacts = page_number.page(p)
            # print(contacts.object_list)
            # print(type(contacts))
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = page_number.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = page_number.page(page_number.num_pages)
        return render(request, "index.html", {"aaa": contacts,'contacts':contacts})

    return render(request, "index.html",{"aaa": contacts,'contacts':contacts})
