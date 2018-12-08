from django import forms

from .models import Photo
from .models import Atom


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('file', )


class AtomForm(forms.ModelForm):
    class Meta:
        model = Atom
        fields = ('file', )
