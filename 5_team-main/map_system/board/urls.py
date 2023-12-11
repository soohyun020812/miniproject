
from django.contrib import admin
from django.urls import path

from . import views 

app_name="board"
urlpatterns = [
    path("list/", views.list, name="list"), #orm방식
    path("list2/<int:pg>/", views.list2, name="list"), 
    path("view/<int:id>/", views.views), 
    path("write/", views.write, name="write"), 
    path("save/", views.save, name="save"), 
    path("modify/", views.modify),
    # 사용자 인풋값 받기 
    # path("userData",views.category_count, name="category_count")
]





