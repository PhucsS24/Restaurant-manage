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
            raise ValidationError('Số điện thoại không hợp lệ')
        return phone

    # Clean method for select_size field
    def clean_select_size(self):
        select_size = self.cleaned_data.get('select_size')
        if select_size < 1:
            raise ValidationError('Số lượng đặt phải lớn hơn 0')
        return select_size

    # Clean method for email field
    def clean_email(self):
        email = self.cleaned_data.get('email')
        allowed_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'example.com']
        if not any(email.endswith('@' + domain) for domain in allowed_domains):
            raise ValidationError(f"Email phải thuộc các tên miền sau: {', '.join(allowed_domains)}")
        return email
    def clean_choice_date(self):
        choice_date = self.cleaned_data.get('choice_date')
        
        # Kiểm tra xem choice_date có phải là ngày tương lai không
        if choice_date <= datetime.date.today():
            raise ValidationError('Ngày đặt bàn phải là ngày tương lai.')
        
        return choice_date
    def clean_note(self):
        note = self.cleaned_data.get('note')
        if not note.strip():  # Loại bỏ khoảng trắng ở đầu và cuối chuỗi
            raise ValidationError('Ghi chú không được để trống')
        return note