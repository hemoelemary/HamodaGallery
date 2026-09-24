from django import forms

class PostForm(forms.Form):
    uploadername = forms.CharField(max_length=250)
    picname = forms.CharField(max_length=250)
    image = forms.FileField()
    details = forms.CharField(widget=forms.Textarea)