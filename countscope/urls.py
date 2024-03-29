from django.urls import path
from . import views

#http://127.0.0.1:8000/  => anasayfa
#http://127.0.0.1:8000/home => anasayfa
#http://127.0.0.1:8000/counter => tanımlama kısmı

urlpatterns = [    
    path('contact', views.contact,name="contact"),
    path('about', views.about,name="about"),
    path("",views.home,name="home"),
    path("anasayfa",views.home,name="home" ),
    path("search",views.search, name="search"),
    path("create", views.create, name="create"),
    path('count-list', views.count_list, name="count_list"),
    path('count-edit/<int:id>', views.count_edit,name="count_edit"),
    path('count-delete/<int:id>', views.count_delete,name="count_delete"),
    path('upload', views.upload, name="upload"),
    path('<str:category_name>', views.getCoursesByCategory, name='courses_by_category'),
]
