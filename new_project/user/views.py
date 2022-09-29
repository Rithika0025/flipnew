from django.shortcuts import render

# Create your views here.
def master_page (request):
    return render (request,'user/masterpg.html')

def flip_home (request):
    return render (request,'user/homepg.html')

def flip_about (request):
    return render (request,'user/aboutpg.html')

def flip_order (request):
    return render (request,'user/orderspg.html')

def flip_login (request):
    return render (request,'user/loginpg.html')

def flip_new (request):
    return render (request,'user/newpage.html')

def flip_box (request):
    return render (request,'user/boxcss.html')

def flip_rules (request):
    return render (request,'user/cssrules.html')

def flip_grid (request):
    return render (request,'user/cssgrid.html')

def flip_gridalign (request):
    return render (request,'user/gridalign.html')

def flip_gridwork (request):
    return render (request,'user/gridwork.html')

def flip_bootstrap (request):
    return render (request,'user/boots.html')

def flip_java (request):
    return render (request,'user/java.html')

def flip_javascript (request):
    return render (request,'user/javascript1.html')

def flip_cssclass (request):
    return render (request,'user/cssclass.html')

def flip_boxnew (request):
    return render (request,'user/boxnew.html')
