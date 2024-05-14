from django import forms

class BookTableForm(forms.Form):
    select_location = forms.CharField(max_length=100)
    select_size = forms.IntegerField()
    choice_date = forms.DateField()
    choice_time = forms.TimeField()
    fname = forms.CharField(max_length=100)
    lname = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    email = forms.EmailField()
    size_party = forms.CharField(max_length=100)
    note = forms.CharField(widget=forms.Textarea)