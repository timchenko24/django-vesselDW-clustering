from django.urls import path
from .views import index, by_vesselType


urlpatterns = [
    path('<int:type_id>', by_vesselType),
    path('', index)
]