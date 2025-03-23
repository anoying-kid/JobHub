from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, JobSeekerProfile, EmployerProfile

class JobSeekerSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'job_seeker'
        if commit:
            user.save()
        return user

class EmployerSignUpForm(UserCreationForm):
    company_name = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'company_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'employer'
        if commit:
            user.save()
            EmployerProfile.objects.create(user=user, company_name=self.cleaned_data.get('company_name'))
        return user

class JobSeekerProfileForm(forms.ModelForm):
    class Meta:
        model = JobSeekerProfile
        fields = ('resume', 'bio')

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = ('company_name', 'company_website', 'company_description')