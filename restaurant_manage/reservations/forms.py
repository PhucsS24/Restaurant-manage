from django import forms
import re
from django.core.exceptions import ValidationError
import datetime
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

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\+?1?\d{9,15}$', phone):
            raise ValidationError('So dien thoai khong hop le')
        return phone

    # Clean method for select_size field
    def clean_select_size(self):
        select_size = self.cleaned_data.get('select_size')
        if select_size < 1:
            raise ValidationError('So luong phải lon hon 0')
        return select_size

    # Clean method for email field
    def clean_email(self):
        email = self.cleaned_data.get('email')
        allowed_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'example.com']
        if not any(email.endswith('@' + domain) for domain in allowed_domains):
            raise ValidationError(f"Email phai thuoc cac mien sau: {', '.join(allowed_domains)}")
        return email

    # Clean method for entire form
    def clean(self):
        cleaned_data = super().clean()
        choice_date = cleaned_data.get('choice_date')
        choice_time = cleaned_data.get('choice_time')
        select_location = cleaned_data.get('select_location')

        # Add any cross-field validation here
        if choice_date and choice_time:
            # Ví dụ kiểm tra xem ngày và giờ có hợp lệ không
            if choice_date < datetime.date.today():
                raise ValidationError('Ngay dat ban phai la tuong lai')
        
        return cleaned_data