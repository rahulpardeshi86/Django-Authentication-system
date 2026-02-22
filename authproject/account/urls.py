from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    # path('', admin.site.urls),
    path('',register_view,name='register'),
    path('login/',Login_view, name='login'),
    path('logout/',logout_view,name='logout'),
    path('dashboard/',dashboard,name='dashboard'),
]