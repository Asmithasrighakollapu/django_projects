from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('firstpage',views.firstpage,name="firstpg"),
    path('secondpage',views.secondpage,name="secondpg"),
    path('temppg',views.htmlproj,name="temppg"),
]