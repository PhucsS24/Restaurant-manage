from django import forms
from .models import CustomUser

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(max_length=254, help_text='Enter a valid email address.')

    error_messages = {
        'password_mismatch': 'The two password fields did not match.',
    }

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone', 'password1', 'password2')
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2


class SignInForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


# class EditProfileForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ('first_name', 'last_name', 'email', 'phone')