from django.urls import path
from . import views

urlpatterns=[
    path('master',views.master_page,name='masterpg'),
    path('',views.flip_home,name='homepg'),
    path('about',views.flip_about,name='aboutpg'),
    path('order',views.flip_order,name='orderspg'),
    path('login',views.flip_login,name='loginpg'),
    path('new',views.flip_new,name='newpage'),
    path('box',views.flip_box,name='boxcss'),
    path('rules',views.flip_rules,name='rulescss'),
    path('grid',views.flip_grid,name='grid'),
    path('grid1',views.flip_gridalign,name='gridalign'),
    path('gridwork',views.flip_gridwork,name='gridwork'),
    path('bootstrap',views.flip_bootstrap,name='bootstrap'),
    path('java',views.flip_java,name='java'),
    path('javascript',views.flip_javascript,name='javascript'),
    path('cssclass',views.flip_cssclass,name='cssc lass'),
    path('boxnew',views.flip_boxnew,name='boxnew'),
]