from django.urls import path
from . import views

urlpatterns = [

    path('cv',views.cv),
    path('bio',views.bio)
]
