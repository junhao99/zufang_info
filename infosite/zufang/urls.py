from django.urls import path

from zufang import views

urlpatterns = [
    path('main_infos/',views.show_main_info ),
    path('first_infos',views.show_info)
]