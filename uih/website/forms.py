from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Patient
from .models import Nurse
class PatientForm(UserCreationForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),max_length=45)
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),max_length=45)
    mi = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MI'}),max_length=1)
    ssn = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SSN'}),max_length=45)
    race = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Race'}),max_length=45)
    age = forms.IntegerField()
    gender = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gender'}),max_length=45)
    occupation_class = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Occupation'}),max_length=45)
    phone_field = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),max_length=45)
    address = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),max_length=100)

    class Meta:
        model = User
        fields = ('username', 'password1','first_name', 'mi', 'last_name', 'ssn', 'address', 'phone_field', 'age', 'gender', 'race', 'occupation_class')
        


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

class NurseUpdateForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = ['fname', 'mi', 'lname', 'gender', 'phone_field', 'address']