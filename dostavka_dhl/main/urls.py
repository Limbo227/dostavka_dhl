from django.urls import path
from .views import *


urlpatterns = [
    path('main/create', MainCreationView.as_view()),
    path('main/list', MainListView.as_view()),
    path('main/scale', ScaleView.as_view()),
    path('main/scale-weight', ScaleWeightView.as_view()),
]