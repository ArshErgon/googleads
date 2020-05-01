from django.urls import path

from . import views

appname = "ads"

urlpatterns = [
    path('', views.desktop_home_page, name="home"),
    path('<int:pk>/', views.desktop_single_page_recipes, name='single'),
]
