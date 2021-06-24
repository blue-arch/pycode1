from django.shortcuts import render
# import class "Topic" from ./models.py
from .models import Topic


# Create your views here.

def index(request):
    """home page of learning log"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """show one topic with its all entry"""
    topic = Topic.objects.get(id=topic_id)
    # minus sign indicates descending sort
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)