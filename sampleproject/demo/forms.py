from django import forms
from django_bootstrap_wysiwyg.widgets import WysiwygInput
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        widgets = {
            'text': WysiwygInput()
        }


class MultipleInputForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=WysiwygInput())
    extra = forms.CharField(widget=WysiwygInput(toolbar_items=[
        'fonts', 'font-sizes', 'alignments']))
