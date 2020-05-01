from django.shorcuts import render 

def desktop_home_page(request):
    return render(request, 'desktop/home/index.html')

def desktop_single_page(request):
    return render(request, 'desktop/single/single_page.html')