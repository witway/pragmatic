from django import forms
from django.forms import ModelForm

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto;'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    # required = False는 선택지에서 안선택한다는 '----'를 넣어줌
    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']