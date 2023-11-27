from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import PatientForm
from .models import Patient

def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        userRole = request.POST['role']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            messages.success(request, "You have heen logged in! You are a " + userRole)
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html')

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
