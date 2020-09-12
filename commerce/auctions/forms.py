from django import forms


from django.forms import ModelForm
from .models import Listing


class CreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['thumbnail'].required = True
        self.fields['title'].required = True
        self.fields['price'].required = True

    class Meta:
        model = Listing
        fields = ['title','summary','price','thumbnail']