from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
data = {
    "photo":"photo kısmı",
    "video":"video kısmı", 
}
def home(request):
    # list_items=""
    # category_list = list(data.keys())

    # for category in category_list:
    #     redirect_url= reverse('courses_by_category',args=[category])
    #     list_items += f"<li><a href = '{redirect_url}'>{category}</a></li>"
    
    # html=f"<h1>seçenek listesi</h1><br><ul>{list_items}</ul>"
    # return HttpResponse(html)    
   return render(request, "index.html")
def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name];    
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("yanlış kategori seçimi")

def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys()) 
    if(category_id > len(category_list)):
        return HttpResponseNotFound("yanlış kategori seçimi")

    category_name = category_list[category_id - 1]

    redirect_url = reverse('courses_by_category', args=[category_name])

    return redirect(redirect_url)