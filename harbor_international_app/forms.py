from django import forms

from .models import Video, Algebra, Geometry

class Video_form(forms.ModelForm):
    class Meta:
        model = Video
        fields = ("caption","content","videofile")

class Algebra_form(forms.ModelForm):
    class Meta:
        model = Algebra
        fields = ("caption","content","videofile")


class Geometry_form(forms.ModelForm):
    class Meta:
        model = Geometry
        fields = ("caption","content","videofile")

