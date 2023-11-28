from typing import Any
from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .forms import NurseUpdateForm

from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import PatientForm
from .models import Patient, TimeSlot, Nurse, PatientSchedule

def home(request):
    patients = Patient.objects.all()
    user = None  # Initialize user to None outside the if block

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_role = request.POST['role']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user_role == 'patient' and hasattr(user, 'patient'):
                login(request, user)
                messages.success(request, "You have been logged in! You are a patient.")
                return redirect('home')
            elif user_role == 'nurse' and hasattr(user, 'nurse'):
                login(request, user)
                messages.success(request, "You have been logged in! You are a nurse.")
                return redirect('nurse_home')
            elif user_role == 'admin' and user.is_staff and user.is_superuser:
                login(request, user)
                messages.success(request, "You have been logged in! You are an admin.")
                return redirect('admin:index')  # Redirect to the Django admin index page
            else:
                messages.error(request, "Invalid role selected.")
        else:
            messages.error(request, "There was an error logging in. Please try again.")

    return render(request, 'home.html', {'patients': patients})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            mi = form.cleaned_data['mi']
            age = form.cleaned_data['age']
            race = form.cleaned_data['race']
            occupation_class = form.cleaned_data['occupation_class']
            phone_field = form.cleaned_data['phone_field']
            address = form.cleaned_data['address']
            ssn = form.cleaned_data['ssn']
            gender = form.cleaned_data['gender']
            user = User.objects.get(username=username)
            patient = Patient.objects.create(user=user, fname= user.first_name, lname=user.last_name, mi=mi, age=age, race=race, occupation_class=occupation_class, phone_field=phone_field, address=address, ssn=ssn, gender=gender)
            patient.save()  

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You are registered.")
            return redirect('home')
    else:
        form = PatientForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

def user_record(request, pk):
    if request.user.is_authenticated:
        user_record = Patient.objects.get(ssn = pk)
        return render(request, 'record.html', {'user_record':user_record})
    else:
        messages.success(request, "There Was An Error Logging In, Please Try Again...")
        return redirect('home')

def schedule_vaccination(request):
    # if request.user.is_authenticated:
    timeslots = TimeSlot.objects.all
        
    return render(request, 'schedule.html',{'timeslots':timeslots})

def schedule_confirm(request,pk):
    if request.user.is_authenticated:
        slot = TimeSlot.objects.get(id=pk)

        return render(request, 'schedule_confirm.html',{'slot':slot})
    messages.success(request, "You must be logged in to schedule.")
    return redirect('home')

def add_schedule(request,pk):
    if request.user.is_authenticated:
        slot = TimeSlot.objects.get(id=pk)
        if request.method == "POST":
            # user = Us
            patient = Patient.objects.get(user=request.user)
            schedule = PatientSchedule.objects.create(time_slot=str(slot), patient_ssn=patient.ssn, id=pk)
            schedule.save()

            messages.success(request, "Vaccination Appointment scheduled!")
            return redirect('home')
        return render(request, 'schedule_confirm.html',{'slot':slot})

class NurseUpdateView(UpdateView):
    model = Nurseform_class = NurseUpdateForm
    form_class = NurseUpdateForm
    template_name = 'update_nurse_info.html'
    success_url = reverse_lazy('nurse_schedule_view')
    def get_object(self, queryset=None):
        return Nurse.objects.get(employee_id=self.kwargs['nurse_id'])
    
class NurseHomeView(View):
    template_name = 'nurse_home.html'

    def get(self, request, *args, **kwargs):
        # Get the logged-in nurse instance
        nurse = Nurse.objects.get(user=request.user)
        return render(request, self.template_name, {'nurse': nurse})
