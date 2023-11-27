from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class PatientForm(UserCreationForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),max_length=45)
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),max_length=45)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1')


    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''

        # self.fields['password2'].widget.attrs['class'] = 'form-control'
        # self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        # self.fields['password2'].label = ''
