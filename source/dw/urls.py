from django.urls import path
from .views import index, by_vesselType


urlpatterns = [
    path('<uuid:type_id>/', by_vesselType, name='by_vesselType'),
    path('', index, name='index'),
]