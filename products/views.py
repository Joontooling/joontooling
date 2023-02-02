from django.shortcuts import render

# Create your views here.
def index(request):
    pass



def main(request):
    return render(request, 'products/main.html')