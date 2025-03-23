from django.contrib.auth.models import AbstractUser
from  django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('job_seeker', 'Job Seeker'),
        ('employer', 'Employer'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLES)

    @property
    def is_job_seeker(self):
        return self.role == 'job_seeker'
    
    @property
    def is_employer(self):
        return self.role == 'employer'

class JobSeekerProfile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='job_seeker_profile')
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    skills = models.ManyToManyField('jobs.Skill', blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
    
class EmployerProfile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='employer_profile')
    company_name = models.CharField(max_length=100)
    company_website = models.TextField()
    company_description = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.company_name}'s profile"