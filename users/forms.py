from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        help_texts = {
            'username': None
        }

    def password_verification(self):
        if (
            len(self.data['password1']) >= 8 and
            self.data['password1'] == self.data['password2']
        ):
            return self.data['password1']
        return False