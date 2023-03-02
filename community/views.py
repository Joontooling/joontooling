from django.shortcuts import render
from .models import Notice
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def index(request):
    return render(request, 'community/index.html')

def notice(request):
    notices = Notice.objects.all().order_by('-pk')
    # Paginator
    page = request.GET.get('page')
    paginator = Paginator(notices, 10)
    page_obj = paginator.page(page)

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)
    
    return render(request, 'community/notice.html',
    {
        "notices": notices,
        "page_obj": page_obj,
        "paginator": paginator,
    })

def question(request):
    return render(request, 'community/question.html')