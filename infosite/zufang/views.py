from django.shortcuts import render


# Create your views here.
def show_main_info(response):
    return render(response,"info_content.html")
def show_info(response):
    return render(response,"index.html")