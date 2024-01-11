# forms.py
from django import forms
from .models import BlogModel
from ckeditor.widgets import CKEditorWidget

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['blog_title', 'blog_content']
        widgets = {
            'blog_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Blog Title'}),
            
        }



class BlogEditForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['blog_title', 'blog_content']

        widgets = {
            'blog_title': forms.TextInput(attrs={'class': 'form-control'}),
            'blog_content': CKEditorWidget(),
        }