from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import JobSeekerSignUpForm, EmployerSignUpForm, JobSeekerProfileForm, EmployerProfileForm
from .models import JobSeekerProfile, EmployerProfile

def home(request):
    return render(request, 'home.html')

def job_seeker_signup(request):
    if request.method == 'POST':
        form = JobSeekerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            JobSeekerProfile.objects.create(user=user)
            login(request, user)
            return redirect('job_seeker_dashboard')
    else:
        form = JobSeekerSignUpForm()
    return render(request, 'registration/job_seeker_signup.html', {'form': form})

def employer_signup(request):
    if request.method == 'POST':
        form = EmployerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('employer_dashboard')
    else:
        form = EmployerSignUpForm()
    return render(request, 'registration/employer_signup.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.is_job_seeker:
        return redirect('job_seeker_dashboard')
    elif request.user.is_employer:
        return redirect('employer_dashboard')
    else:
        return redirect('admin:index')

@login_required
def job_seeker_dashboard(request):
    if not request.user.is_job_seeker:
        return redirect('home')
    profile = JobSeekerProfile.objects.get(user=request.user)
    return render(request, 'dashboard/job_seeker.html', {'profile': profile})

@login_required
def employer_dashboard(request):
    if not request.user.is_employer:
        return redirect('home')
    profile = EmployerProfile.objects.get(user=request.user)
    return render(request, 'dashboard/employer.html', {'profile': profile})