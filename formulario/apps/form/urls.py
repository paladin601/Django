from django.urls import path
from . import views

app_name='formulario'
urlpatterns = [
    path('', views.index,name='index'),
    path('/detail', views.detail,name='detail'),
    path('/delete', views.delete,name='delete'),
    path('update/<int:id>', views.update,name='update'),
]