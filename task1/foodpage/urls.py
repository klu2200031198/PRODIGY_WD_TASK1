from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
      path('',views.projecthomepage, name = 'projecthomepage'),
      path('breakfasthomepage',views.breakfasthomepage, name= 'breakfasthomepage'),
      path('lunchhomepage',views.lunchhomepage, name = 'lunchhomepage'),
]