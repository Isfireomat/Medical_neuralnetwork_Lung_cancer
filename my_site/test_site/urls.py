from django.urls import path
from .views import *

urlpatterns=[
path('',index.as_view()),
path('api/AI/', my_view, name='AI'),
]