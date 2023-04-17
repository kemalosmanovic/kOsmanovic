from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100, required=True)
    email = forms.EmailField(label='Your Email', max_length=100, required=True)
    subject = forms.CharField(label='Subject', max_length=200, required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'rows': 5}), required=True)
