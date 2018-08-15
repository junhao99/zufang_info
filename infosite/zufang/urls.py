from django.urls import path

from zufang import views

urlpatterns = [

    path('infos/content/<int:info_id>', views.show_content, name='content'),
    path('infos/normal/<int:number>', views.show_info, name='allinfos'),
    path('infos/map', views.show_map, name='map'),
    path('infos/price/<int:number>', views.show_index_by_price, name='info_price'),
    path('page/<int:one_page>', views.page, name='onepage'),
    path('infos/search', views.user_seacrch, name="ss"),
    path('infos/page/<int:number>',views.info_page,name='page_num'),
    path('user/info',views.user_add_info,name = "add_zf_info"),
]
