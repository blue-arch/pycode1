"""define url mode of learning_logs"""

from django.urls import path, re_path
from . import views

urlpatterns = [
    # home
    path('', views.index, name='index'),
    # topics
    path('topics/', views.topics, name='topics'),
    re_path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
]
app_name = 'learning_logs'
