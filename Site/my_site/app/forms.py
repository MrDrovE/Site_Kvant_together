from django import forms
from .models import Category

from django.urls import reverse_lazy


class ChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.title
