from django.shortcuts import render

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
