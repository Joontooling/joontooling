from django.shortcuts import render
from .models import Notice
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def index(request):
    return render(request, 'community/index.html')

def notice(request):
    notices = Notice.objects.all().order_by('-pk')
    # Paginator
    page = request.GET.get('page', 1)
    paginator = Paginator(notices, 10)
    page_obj = paginator.page(page)

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    
    return render(request, 'community/notice.html',
    {
        "notices": notices,
        "page_obj": page_obj,
        "paginator": paginator,
    })

def question(request):
    return render(request, 'community/question.html')

def qna(request):
    return render(request, 'community/qna.html')

def qna_list(request):
    return render(request, 'community/qna_list.html')
