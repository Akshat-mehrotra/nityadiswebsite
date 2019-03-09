from django import forms

from .models import Commission, Art

class Art_get_form(forms.ModelForm):
    class Meta:
        model = Commission
        exclude = ('art',)

class Upload_art_form(forms.ModelForm):
    class Meta:
        model = Art
        fields = '__all__'
