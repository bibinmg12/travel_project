from django.urls import path

from . import views

urlpatterns = [
   
    path('',views.demo,name='demo'),
    # path('teams/',views.teammates,name='teammates'),
    # path('add/',views.addition,name='addition'),
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact')
]
