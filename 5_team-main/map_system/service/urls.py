
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'service'

urlpatterns = [
    path("index/", views.index),
    path("map/", views.show_map, name='map'),
    path("write/", views.write),
    path("save/", views.save),
    path("test/", views.user_input_view),
    path("report/",views.generate_report),
    path("custom_sql_query/",views.custom_sql_query),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login, name='login'),

]

