from django import forms
from .models import BlogComment, Suggest, Imitate


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['user_name', 'body']
        widgets = {
                   'user_name': forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'please input name',
                                'aria-describedby': 'sizing-addon1',
                                }),
                   'body': forms.Textarea(attrs={
                                'placeholder': 'let me say',
                                'class': 'form-control',
                                'rows': 4,
                                }),
                   }


class SuggestForm(forms.ModelForm):
    class Meta:
        model = Suggest
        fields = ['suggest']
        widgets = {
            'suggest': forms.Textarea(attrs={
                'placeholder': 'write down your suggest',
                'class': 'form-control',
                'rows': 4,
                'cols': 80,
                })
        }


class ImitateForm(forms.ModelForm):
    class Meta:
        model = Imitate
        fields = ['imitate_name']
        widgets = {
                   'imitate_name': forms.Textarea(attrs={
                        'placeholder': 'write something',
                        'class': 'form-control',
                        'rows': 3,
                        })
                   }
        