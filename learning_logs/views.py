
from django.shortcuts import render
from .models import Topic 
from .form import TopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    """Página principal do learning Log."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Mostra todods os assuntos."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context )


def topic(request, topic_id):
    """Mostra um único assunto e todas as suas entradas."""
    topic = Topic.objects.get(id = topic_id) 
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Adiciona um novo assunto."""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
         if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topcis'))
    context = {'form' : form}
    return render(request, 'learning_logs/new_topic.html', context)
    