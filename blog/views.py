from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from .models import Article,Comment,NewUser,Tag,Category,Author,Train
from .forms import LoginForm,CommentForm,RegisterForm,SetInfoForm,SearchForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from urllib.parse import urljoin
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.list import ListView
from rest_framework.decorators import api_view
from .search import train
import markdown2
import django_filters
from rest_framework import viewsets,filters
from rest_framework.response import Response
from .Serialzier import AuthorSeralizer,CategorySeralizer,TrainSeralizer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSeralizer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySeralizer

class TrainViewSet(viewsets.ModelViewSet):
    queryset = Train.objects.all()
    serializer_class = TrainSeralizer

@api_view(['GET','POST','DELETE'])
def train_detail(request):
    if request.method == 'GET':
        f = request.GET.get('from_station')
        t = request.GET.get('to_station')
        date = request.GET.get('date')
        Train.objects.filter().delete()
        ta = train(f,t,date)
        ta.search()
        result = Train.objects.filter(date=date)
        serializer = TrainSeralizer(result,many=True)
        return Response(serializer.data)

def index(request):
    article_list = Article.objects.query_by_time()
    loginform = LoginForm()
    tag_list = Tag.objects.all().order_by('name')
    context = {'article_list':article_list,
               'tag_list': tag_list,
               'loginform':loginform,
               }
    return render(request,'index.html',context)

def log_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'login.html',{'form':form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['uid']
            password = form.cleaned_data['pwd']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                url = request.POST.get('source_url','/blog')
                return redirect(url)
            else:
                return render(request,'login.html',{'form':form ,'error':"用户名或密码不正确"})
        else:
            return render(request,'login.html',{'form':form})

@login_required
def log_out(request):
    url = request.POST.get('source','/blog/')
    logout(request)
    return redirect(url)

def article(request,article_id):
    article = get_object_or_404(Article,id=article_id)
    content = markdown2.markdown(article.content,extras=["code-friendly","fenced-code-blocks","header-ids","tocs","metadata"])
    commentform = CommentForm()
    loginform = LoginForm()
    comments = article.comment_set.all
    tag_list = Tag.objects.all().order_by('name')

    return render(request,'article_page.html',{
        'article':article,
        'loginform':loginform,
        'commentform':commentform,
        'content':content,
        'comments':comments,
        'tag_list': tag_list,
    })

class TagView(ListView):
    template_name = 'index.html'
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = Article.objects.filter(tags=self.kwargs['tag_id'])
        return article_list

    def get_context_data(self,**kwargs):
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        kwargs['category_list'] = (Category.objects.all().order_by('name'))
        name = get_object_or_404(Tag,pk=self.kwargs['tag_id'])
        kwargs['tag_name'] = name
        return super(TagView,self).get_context_data(**kwargs)

@login_required()
def comment(request,article_id):
    form = CommentForm(request.POST)
    url = urljoin('/blog/',article_id)
    if form.is_valid():
        user = request.user
        article = Article.objects.get(id=article_id)
        new_comment = form.cleaned_data['comment']
        c = Comment(content=new_comment,article_id=article_id)
        c.user = user
        c.save()
        article.comment_num += 1
        article.save()
    return redirect(url)

def register(request):
    invalid = "用户名已存在"
    valid = "用户名可用"

    if request.method == 'GET':
        form = RegisterForm()
        return render(request,'register.html',{'form':form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if request.POST.get('raw_username','erjgiqfv240hqp5668ej23foi') != 'erjgiqfv240hqp5668ej23foi':
            try:
                user = NewUser.objects.get(username=request.POST.get('raw_username',''))
            except ObjectDoesNotExist:
                return render(request,'register.html',{'form':form,'msg':valid})
            else:
                return render(request,'register.html',{'form':form,'msg':invalid})

        else:
            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if password1 != password2:
                    return render(request,'register.html',{'form':form,'msg':"密码不一致"})
                else:
                    user = NewUser.objects.create_user(username,email,password1)
                    return redirect('/blog/login')
            else:
                return render(request,'register.html',{'form':form})





