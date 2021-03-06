from django.shortcuts import render, redirect
from django.http import Http404

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from django.contrib.auth.models import User

from ideabox.serializers import IdeaSerializer, UserSerializer

from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Idea, IdeaForm, Comment, CommentForm

from django.contrib.auth.decorators import login_required

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    paginate_by = 100

class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all().order_by('-date_added')
    serializer_class = IdeaSerializer

def index(request):
    ideas = Idea.objects.all().order_by('-date_added')
    context = RequestContext(request, {'ideas' : ideas, })
    return render(request, 'ideabox/index.html', context)

def ShowIdea(request, id):
    try:
        instance = Idea.objects.get(id=id)
    except:
        raise Http404('Idea does not exists!')

    context = RequestContext(request, {'idea' : instance, })
    return render(request, 'ideabox/idea.html', context)

@login_required
def NewIdea(request):
    if request.method == 'POST':
        idea_form = IdeaForm(request.POST)
        if idea_form.is_valid():
            idea = idea_form.save(commit=False)
            idea.author = request.user
            idea.save()
    else:
        idea_form = IdeaForm()

    context = RequestContext(request, {'idea_form' : idea_form, })
    return render(request, 'ideabox/add.html', context)

@login_required
def EditIdea(request, id):
    try:
        instance = Idea.objects.get(id=id)
    except:
        raise Http404('Idea does not exists!')
    
    if request.user != instance.author:
        return redirect('/')

    idea_form = IdeaForm(request.POST or None, instance = instance)

    context = RequestContext(request, {'idea_form' : idea_form, })

    if idea_form.is_valid():
        idea = idea_form.save(commit=False)
        idea.save()
        context.push({'success_message' : 'Idea edited successfully' })

    return render(request, 'ideabox/add.html', context)
