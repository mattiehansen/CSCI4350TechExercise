from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('delete/<id>', views.delete, name='delete'),
    path('checkoff/<id>', views.checkoff, name='checkoff'),
    path('uncheck/<id>', views.uncheck, name='uncheck'),
    path('deleteall', views.deleteall, name='deleteall'),
]