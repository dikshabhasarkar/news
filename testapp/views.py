from django.shortcuts import render

# Create your views here.
# first comit

def home_page_view(request):
    return render(request,'testapp/home.html')
