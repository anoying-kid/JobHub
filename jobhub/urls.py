from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('signup/job-seeker/', user_views.job_seeker_signup, name='job_seeker_signup'),
    path('signup/employer/', user_views.employer_signup, name='employer_signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', user_views.dashboard, name='dashboard'),
    path('dashboard/job-seeker/', user_views.job_seeker_dashboard, name='job_seeker_dashboard'),
    path('dashboard/employer/', user_views.employer_dashboard, name='employer_dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)