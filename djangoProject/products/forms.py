from django import forms
from .models import *

#
# class SubscriberForm(forms.ModelForm):
#
#     class Meta:
#         model = Subscriber
#         exclude = [""]

from .models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')