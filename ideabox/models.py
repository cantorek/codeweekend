from django.db import models
from django.conf import settings

from django.forms import ModelForm, Textarea, CharField, ModelChoiceField

from datetime import datetime

# Create your models here.

class Idea(models.Model):
    DIFFICULTY_CHOICES = (
        (1, 'Easy'),
        (2, 'Medium'),
        (3, 'Hard'),
        (4, 'Ultra'),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    date_added = models.DateTimeField('date added', default=datetime.now)
    difficulty = models.PositiveSmallIntegerField(choices=DIFFICULTY_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.title

class IdeaForm(ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'description', 'difficulty']
        widgets = {
                'description' : Textarea(attrs={'cols' : 42, 'rows' : 8, 'class' : 'form-control'}),
                }

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, unique=True)
    idea = models.ForeignKey(Idea)
    description = models.CharField(max_length=2000)

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['description', 'idea']
