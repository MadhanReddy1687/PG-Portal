from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index,name="index"),
    path('areas/<int:city_id>/',views.json_area_response,name='areas'),
    path('details/<str:areas_id>,<str:for_type>,<str:food>,<str:sharing>,<int:prince_range>/',views.json_details_response,name="details"),
    path('images/<int:pg_id>',views.images,name='images')
]