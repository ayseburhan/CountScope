from datetime import date
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import CountScope
# Create your views here.
data = {
    "photo":"photo kısmı",
    "video":"video kısmı", 
}
db ={
       "secenekler": [
           {
        "title":"photo ",
        "description":"photo kısmı açıklaması",
        "imageUrl":"https://www.shaip.com/wp-content/uploads/2022/05/Blog_What-is-AI-Image-Recognition-1.jpg",
        "slug":"photo-kısmı",
        "date": date(2023,12,27),
},
{
               
        "title":"video kısmı",
        "description":"video kısmı açıklaması",
        "imageUrl":"https://www.shaip.com/wp-content/uploads/2022/05/Blog_What-is-AI-Image-Recognition-1.jpg",
        "slug":"photo-kısmı",
        "date": date(2023,12,27),
}
],
"categories" : [
    
        {"id":1, "name ": "photo" , "slug": "photo" },
        {"id":2, "name ": "video" , "slug": "video" },
    
]
} 
    
def home(request):  
   secenekler = CountScope.objects.all()
   kategori = db["categories"]
   return render(request, "index.html",{
       'secenekler': secenekler,
       'kategori': kategori
   })

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name];
        return render(request,'seçenekler.html',{
            'category' : category_name,
            'category_text' : category_text
        })
    except:
        return HttpResponseNotFound("yanlış kategori seçimi")

def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys()) 
    if(category_id > len(category_list)):
        return HttpResponseNotFound("yanlış kategori seçimi")

    category_name = category_list[category_id - 1]

    redirect_url = reverse('courses_by_category', args=[category_name])

    return redirect(redirect_url)