from django.shortcuts import render
from .forms import CreateBlog

# Create your views here.
def index(request):
    return render(request, 'index.html')
def blogMain(request):
    return render(request, 'blogMain.html')
def createBlog(request):
    form = CreateBlog()
    # 세번째인자 [context]를 보내는 것이며, 딕셔너리 자료형의 형태암
    return render(request, 'createBlog.html',{'form': form })
def signin(request):
    return render(request, 'signin.html')
