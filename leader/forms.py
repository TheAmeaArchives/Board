from django import forms
from .models import Curation

class CurationForm(forms.ModelForm):
    class Meta:
        model = Curation
        fields = ('title','sub_title','text',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Curation
        fields = ['title']
        