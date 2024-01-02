from django.urls import path
from . import views

#http://127.0.0.1:8000/  => anasayfa
#http://127.0.0.1:8000/home => anasayfa
#http://127.0.0.1:8000/counter => tanımlama kısmı

urlpatterns = [    
    path('contact', views.contact),
    path('about', views.about),
    path("",views.home),
    path("anasayfa",views.home ),
    path("search",views.search, name="search"),
    path("create", views.create, name="create"),
    path('<int:category_id>', views.getCoursesByCategoryId),
    path('<str:category_name>', views.getCoursesByCategory, name='courses_by_category'),
]
