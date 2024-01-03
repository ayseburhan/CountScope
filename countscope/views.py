from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import  HttpResponseNotFound 
from django.urls import reverse
from countscope.forms import CountScopeCreateForm, CountScopeEditForm
from .models import CountScope
import random
import os
from django.contrib.auth.decorators import login_required, user_passes_test
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
        "isActive": True,
        "date": datetime.now(),
},
{
               
        "title":"video kısmı",
        "description":"video kısmı açıklaması",
        "imageUrl":"https://www.shaip.com/wp-content/uploads/2022/05/Blog_What-is-AI-Image-Recognition-1.jpg",
        "slug":"photo-kısmı",
        "isActive": True,
        "date": datetime.now(),
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

#admin olup olmadığını kontrol eder
def isAdmin(user):
    return user.is_superuser

@user_passes_test(isAdmin)
def create(request):
    # Eğer HTTP isteği POST ise (yani kullanıcı formu doldurup gönderdiyse)
    if request.method == "POST":
        # Form, kullanıcı tarafından gönderilen POST verileriyle oluşturuluyor
        form = CountScopeCreateForm(request.POST, request.FILES)
        if form.is_valid():
            # Form geçerliyse, yeni CountScope nesnesi veritabanına kaydediliyor
            form.save()
            # Kullanıcı ana sayfaya yönlendiriliyor
            return redirect("/anasayfa")
    else:
        # Eğer HTTP isteği POST değilse (GET gibi), boş bir form oluşturuluyor
        form = CountScopeCreateForm()

    # Form, render edilerek HTML şablonuna gönderiliyor
    return render(request, "create.html", {"form": form})

@login_required()
def count_list(request):
    counts = CountScope.objects.all()
    return render(request, 'count-list.html', {
        'counts': counts
    })


def count_edit(request, id):
    count = get_object_or_404(CountScope, pk=id)

    if request.method == "POST":
        form = CountScopeEditForm(request.POST, instance=count)
        form.save()
        return redirect("count_list")
    else:
        form = CountScopeEditForm(instance=count)

    return render(request, "edit-count.html", { "form":form })

def count_delete(request, id):
    count = get_object_or_404(CountScope, pk=id)

    if request.method == "POST":
        count.delete()
        return redirect("count_list")

    return render(request, "count-delete.html", { "count":count })

def upload(request):
    if request.method == "POST":
        uploaded = request.FILES.getlist("images")
        for file in uploaded:
            handle_uploded_files(file)
        return render(request, "success.html")
    return render(request, "upload.html")

def handle_uploded_files(file):
    number=random.randint(1,999)
    #filename _ 213.jpg
    filename, file_extention = os.path.splitext(file.name)
    name = filename + "_" + str(number) + file_extention 
    with open("temp/"+ name,"wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)
def search(request):

    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        counts = CountScope.objects.filter(isActive=True, title__icontains=q).order_by("date")
    return render(request, 'list.html', {'counts': counts, 'query': q})

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