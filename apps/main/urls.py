from django.urls import path
from .views import post_list, my_view

urlpatterns = [
    path('', post_list),
]