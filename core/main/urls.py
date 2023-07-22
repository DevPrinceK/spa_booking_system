from django.urls import path
from .views import *


app_name = "main"
urlpatterns = [
    path('', BaseView.as_view(), name="base"),
    # path(),
]
