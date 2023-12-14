from django.urls import path
from .views import index, order, create, update

urlpatterns = [
    path('', index, name='home'),
    path('order', order, name='order'),
    path('create', create, name='create'),
    path('update/<int:id>', update, name='update'),

]