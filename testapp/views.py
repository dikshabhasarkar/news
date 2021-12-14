from django.shortcuts import render

# Create your views here.
# first comit
# second commit

def home_page_view(request):
    return render(request,'testapp/home.html')
