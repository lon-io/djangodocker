from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    text = forms.CharField(label='Content', max_length=2000)
