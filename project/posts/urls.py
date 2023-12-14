from django.urls import path
from .views import index, create, update, state

urlpatterns = [
    path('', index, name='home'),
    path('create', create, name='create'),
    path('update/<int:id>', update, name='update'),
    path('state/<int:id>', state, name='state')
]