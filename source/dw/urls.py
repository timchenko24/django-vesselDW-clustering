from django.urls import path
from .views import *


urlpatterns = [
    path('vessels/type=<uuid:type_id>/', by_type, name='by_type'),
    path('vessels/', vessels_index, name='vessels_index'),
    path('<str:page>', other_page, name='other'),
    path('', index, name='index'),
]