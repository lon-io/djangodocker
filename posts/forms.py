from django import forms

class PostForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        is_edit_mode = getattr(self, 'is_edit_mode', None)
        if is_edit_mode:
            self.fields['title'].widget.attrs['readonly'] = True

    title = forms.CharField(label='Title', max_length=100)
    text = forms.CharField(label='Content', max_length=2000)
