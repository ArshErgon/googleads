from django.urls import path

from . import views

app_name = "ads"

urlpatterns = [
    path('desktop/', views.desktop_home_page, name="desktop_home_page"),
    path('<slug:slug_title>/', views.desktop_single_page_recipes, name='desktop_single_page_recipes'),
    path('', views.mobile_home_page, name="mobile_home"),
]
