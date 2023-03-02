from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'community/index.html')

def notice(request):
    return render(request, 'community/notice.html')

def question(request):
    return render(request, 'community/question.html')