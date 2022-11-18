from django.urls import path

from webapp.api import add, subtract, multiply, divide
from webapp.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', add, name='add'),
    path('subtract/', subtract, name='subtract'),
    path('multiply/', multiply, name='multiply'),
    path('divide/', divide, name='divide')
]
