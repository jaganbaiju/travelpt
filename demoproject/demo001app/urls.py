from  . import views
from django.urls import path

urlpatterns = [
    path('',views.input,name='input'),
    path('opr/',views.output,name='output')
]