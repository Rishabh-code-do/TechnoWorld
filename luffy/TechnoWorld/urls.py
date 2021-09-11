from django.urls import path

from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('why',views.why, name='why'),
    path('about',views.about,name='about'),
    path('product',views.product,name='product'),
    path('category/<int:id>/',views.category,name='category')
]