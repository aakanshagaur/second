from django import forms




choices = [
    ('education', 'Education'),
    ('politics','Plolitics'),
    ('medical','Medical'),
    ('sport', 'Sport'),
    ('games','Games'),
    ('entertainment', 'Entertainments')
]
 


class Blog(forms.Form):
    title = forms.CharField(max_length= 100)
    post = forms.CharField(widget = forms.Textarea)
    category = forms.CharField(widget = forms.Select(choices = choices))





   