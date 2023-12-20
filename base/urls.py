from django.urls import path
from .views import HomePageView


urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('<str:lang>',HomePageView.as_view(),name='home'),
    # path('about',about,name = 'about')
]