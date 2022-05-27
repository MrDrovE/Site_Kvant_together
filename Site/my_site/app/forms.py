from django import forms
from django.forms import Textarea
from .models import Comments


#Create your forms here.


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('content',)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields[field].widget = Textarea(attrs={'rows':5})