from unicodedata import name
from django.urls import path
from . import views 
from candidate import views as cviews

urlpatterns = [
    path('',cviews.index,name="home"),
    path('login',views.login_request,name="login"),
    path('register',views.register_request,name="register"),
    path('logout',views.logout_request,name="logout"),
    path('about',cviews.about,name = "about"),
    path('favorites',cviews.favorites,name = "favorites"),
    
]
