from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request) -> HttpResponse:
    context: dict [str,str]={'title':'Home','content':"Главная страница - Homer"}
    return render(request,'main/index.html',context)

def about(request):
    return HttpResponse('About pager')