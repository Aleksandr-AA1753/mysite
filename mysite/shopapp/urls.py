from django.urls import path
from shopapp import views

app_name = 'shopapp'

urlpatterns = [
    path('create/',
                    views.tovar_create,
                    name='tovar_create'
                    ),
    path('', views.index, name='index'),
]