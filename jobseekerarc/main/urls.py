from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('jobrecruiter-home', views.jobrecruiter_home, name='jobrecruiter_home'),
    path('jobseeker-login', views.jobseeker_login, name='jobseeker_login'),
    path('jobrecruiter-login', views.jobrecruiter_login, name='jobrecruiter_login'),
    path('jobseeker-sign-up', views.jobseeker_sign_up, name='jobseeker_sign_up'),
    path('jobrecruiter-sign-up', views.jobrecruiter_sign_up, name='jobrecruiter_sign_up'),
    path('create-job', views.create_job, name='create_job'),
    path('job-applications', views.get_job_applications, name='job_applications'),
    path('applied-jobs', views.get_applied_jobs, name='applied_jobs'),
    path('job-detail/<str:id>', views.job_detail, name='job_detail'),
    path('job-applications/<str:id>', views.view_job_application, name='job_application'),
]
