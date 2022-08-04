from django import forms
from .models import TodoModel


class TodoModelForm(forms.ModelForm):
    title = forms.CharField(
        max_length=255,
        widget=(
            forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Title'
                }
            )
        )
    )

    description = forms.CharField(
        widget=(
            forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Description'
                }
            )
        )
    )


    class Meta:
        model = TodoModel
        fields = ['title', 'description',]