from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import request, HttpResponse
from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from zufang.models import Zufang_Info


def info_page(requset, number):
    dict1 = {}
    # res = Zufang_Info.objects.filter(title__range=(number * 10, (number + 1) * 10))
    res = Zufang_Info.objects.order_by("month_money").all()[10 * (number - 1):10 * number]
    dict1["aaa"] = res
    print(res)
    return render(requset, "index.html", dict1)


def show_index_by_price(request, number):
    dict1 = {}
    count = Zufang_Info.objects.all().count()
    print(count)
    page_number = int(count / 10) + 1
    print(page_number)
    print("dddddddddddddddd")
    # Show 10 contacts per page
    res = Zufang_Info.objects.order_by("month_money").all()[10 * (number - 1):10 * number]

    # res = Zufang_Info.objects.all()[:10]
    dict1["aaa"] = res
    num = [i for i in range(1, page_number + 1)]
    print(num)
    dict1["page_number"] = num
    name = 'info_price'
    dict1["page_name"] = name

    return render(request, "index.html", dict1)


def show_content(request, info_id):
    # s = Zufang_Info(title = "1",month_money = "100",mianji = "100")
    contact_list = Zufang_Info.objects.all()
    dict1 = {}

    # res = Zufang_Info.objects.all()
    res = Zufang_Info.objects.get(id=info_id)
    dict1["info"] = res

    return render(request, "info_content.html", dict1)


def show_info(request, number):
    # index infomation
    dict1 = {}
    # page_number = Paginator(contact_list, 10)
    count = Zufang_Info.objects.all().count()
    print(count)
    page_number = int(count / 10) + 1
    print(page_number)
    print("dddddddddddddddd")
    # Show 10 contacts per page
    res = Zufang_Info.objects.all()[10 * (number - 1):10 * number]

    # res = Zufang_Info.objects.all()[:10]
    dict1["aaa"] = res
    num = [i for i in range(1, page_number + 1)]
    print(num)
    dict1["page_number"] = num
    name = 'allinfos'
    dict1["page_name"] = name
    return render(request, "index.html", dict1)


def page(request, one_page):
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
        return render(request, "index.html", {"aaa": contacts, 'contacts': contacts})

    return render(request, "index.html", {"aaa": contacts, 'contacts': contacts})


def user_seacrch(request):
    p = request.POST["search_content"]
    dict1 = {}
    res = Zufang_Info.objects.filter(Q(title__contains=p) | Q(address__contains=p) | Q(city_address__contains=p))

    dict1["aaa"] = res
    return render(request, "index.html", dict1)


def show_map(request):

    return render(request, "map.html")


def user_add_info(request):
    if request.POST:
        a = request.POST["title"]
        request.session["id"] = 1
        return HttpResponse("a")
    return render(request, "add_zufanginfo.html")
