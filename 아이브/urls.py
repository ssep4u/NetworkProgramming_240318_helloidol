from django.urls import path

from 아이브 import views

app_name = '아이브'

urlpatterns = [
    path('유진/', views.show_유진, name='유진'),
    path('원영/', views.show_원영, name='원영'),
]