from unicodedata import name
from django.urls import path
from . import views
from account import views as account_views
urlpatterns = [
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("details",views.search_for_candidate,name="search"),
    path("add-favourite/<str:username>",views.add_favorite,name="add-favorites"),
    path("favorites",views.favorites,name="favorites"),
    path("logout",account_views.logout_request),
]
