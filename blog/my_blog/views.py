from django.shortcuts import render,render_to_response
from django.template import RequestContext
from my_blog.models import Article
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from my_blog.forms import ContactForm 


def home(request):

    articles = Article.objects.all()
    return render(request,'index.html',locals())

def message(request):

    return render(request,'message.html')

def detail(request,year,month,day,id):
    article = Article.objects.get(id=str(id))

    return render(request,'content.html',locals())

def about(request):    
    return render(request,'about.html',locals())

def archive(request):
    archive = Article.date_list.get_Article_OnArchive()
    ar_newpost = Article.objects.order_by('-publish_time')[:10]
    date_list = Article.date_list.get_Article_onDate()

    return render(request,'archive.html',locals())

def blog_search(request):
    is_search = True
    
    error = False
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'index.html',locals())
        else:
            articles = Article.objects.filter(title__icontains = s)
            if len(articles) == 0:
                error = True
    return render(request,'index.html',locals())

def submit_done(request):
    return render(request,'submit_done.html',locals())

def submiting(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                    cd['name'],
                    cd['message'],
                    cd.get('email','18717831373@163.com'),
                    ['18717831373@163.com'],
                    )
            return HttpResponseRedirect('/submit_done/')
    else:
        form =ContactForm()
    return render(request,'about.html',locals())

# Create your views here.
