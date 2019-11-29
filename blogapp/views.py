from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBlog
from .models import Blog, Comment
from .forms import BlogCommentForm
from django.contrib.auth.models import User #User 모델을 사용하기위해 선언해준다.
from django.contrib import auth


# Create your views here.
def index(request):
    return render(request, 'index.html')


def blogMain(request):
    return render(request, 'blogMain.html')


def createBlog(request):
    if request.method == 'POST':
        form = CreateBlog(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blogMain')
        else:
            return redirect('index')
    else:
        form = CreateBlog()
        # 세번째인자 [context]를 보내는 것이며, 딕셔너리 자료형의 형태임
        return render(request, 'createBlog.html', {'form': form})


def blogMain(request):
    blogs = Blog.objects.all()  # 저장된 객체를 모 가리키는 객체 'blogs'를 만듬
    return render(request, 'blogMain.html', {'blogs': blogs})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(blog_id=blog_id)

    if request.method == 'POST':
        comment_form = BlogCommentForm(request.POST)

        if comment_form.is_valid():
            content = comment_form.cleaned_data['comment_textfield']

            print(content)

            login_request_uri = 'https://kauth.kakao.com/oauth/authorize?'

            client_id = '187fc792a19f9586952c9a8527459053'
            redirect_uri = 'http://127.0.0.1:8000/oauth'

            login_request_uri += 'client_id=' + client_id
            login_request_uri += '&redirect_uri=' + redirect_uri
            login_request_uri += '&response_type=code'

            return redirect('login_request_uri')
        else:
            return redirect('blogMain')

    else:
        comment_form = BlogCommentForm()

        context = {
            'blog_detail': blog_detail,
            'comments': comments,
            'comment_form': comment_form
        }

        return render(request, 'detail.html', context)


def oauth(request):
    code = request.GET['code']
    print('code = ' + str(code))
    return redirect('blogMain')


def signup(request):
    if request.method == "POST":
        user = User.objects.create_user(
            email=request.POST["email"], password=request.POST["password"], username=request.POST["username"])
        auth.login(request, user)
        return redirect('complete.html')
    return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email=email, password= password)
        if user is not None:
            auth.login(request, user)
            return redirect('blogMain.html')
        else:
            print("ddddd")
            return render(request, 'signin.html', {'error' : '올바르지 않은 이름 패스워드입니다.'})
    else:
        return render(request, 'signup.html')


def survey(request):
    return render(request, 'survey.html')

def complete(request):
    return render(request, 'complete.html')