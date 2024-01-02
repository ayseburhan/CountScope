from django import forms
from django.forms import TextInput, Textarea
from countscope.models import CountScope

# class CountScopeCreateForm(forms.Form):
#     title = forms.CharField(
#         required=True, 
#         error_messages= {
#         "required":"kurs başlığı girmelisiniz."}, 
#         widget=forms.TextInput(attrs={"class": "form-control"}))
    
#     description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
#     slug = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
class CountScopeCreateForm(forms.ModelForm):
    class Meta:
        model = CountScope
        fields = ('title','description','slug')
        labels = {
            'title':"Başlık",
            'description':'Açıklama'
        }
        widgets = {
            "title": TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
            "slug": TextInput(attrs={"class":"form-control"}),
        }
        error_messages = {
            "title": {
                "required":"Başlığı girmelisiniz.",
                "max_length": "maksimum 50 karakter girmelisiniz"
            },
            "description": {
                "required":"çıklaması gereklidir."
            }
        }
        