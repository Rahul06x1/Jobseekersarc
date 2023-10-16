from django.shortcuts import render, redirect
# from .forms import RegisterForm, JobForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Job, JobSeeker, JobRecruiter, JobApplication
from .decorators import job_seeker_access_only, job_recruiter_access_only
# from .forms import UploadJobApplicationForm
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.models import User
# from django.conf import settings
# User = settings.AUTH_USER_MODEL
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# def register_user(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             usertype = form.cleaned_data.get('usertype')
#             user = User.objects.get(username=username)
#             user_data = UserData.objects.create(user=user, usertype=usertype)
#             user_data.save()
#             print('kkkkkkkkk')
#             return redirect('main/home.html')
#     else:
#         form = RegisterForm()
#     return render(request, 'registration/sign_up.html', {'form': form})


# Create your views here.
# @login_required(login_url='/login')
@job_seeker_access_only()
@login_required(login_url='/jobseeker-login')
def home(request):
    print('aaaaa', request.user.email)
    # jobseeker = JobSeeker.objects.get(user_id=request.user.id)
    # print('lll',jobseeker,jobseeker.is_jobseeker)
    # print('aaaaa', request.user.id)
    # print('aaaaa', request.user.password)
    # print('aaaaa', request.user.username)
    # print('aaaaa', request.user.is_authenticated)
    # user = User.objects.filter(id=request.user.id).first()
    # print('ll', user.usertype)
    jobs = Job.objects.all()

    if request.method == 'POST':
        job_id = request.POST.get('job-id')
        job = Job.objects.filter(id=job_id).first()
        print(job, 'llll')
    return render(request, 'main/home.html', {'jobs': jobs})


@job_recruiter_access_only()
@login_required(login_url='/jobrecruiter-login')
def jobrecruiter_home(request):
    # jobs = Job.objects.all()
    jobs = {}
    job_exists = Job.objects.filter(author_id=request.user.id).exists()
    if job_exists:
        jobs = Job.objects.filter(author_id=request.user.id)
    if request.method == 'POST':
        job_id = request.POST.get('job-id')
        job = Job.objects.filter(id=job_id).first()
        if job and job.author == request.user:
            job.delete()
    print('okl', jobs)
    return render(request, 'main/jobrecruiter_home.html', {'jobs': jobs})


def jobseeker_login(request):
    if request.method == 'POST':
        try:
            password = request.POST['password']
            username = request.POST['username']
            user = authenticate(request, username=username, password=password)
            user_status = JobSeeker.objects.get(user_id=user.id)
            if user is not None and user_status.is_jobseeker:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse('Invalid credentials')
        except Exception:
            return HttpResponse('Invalid username or password')
    return render(request, 'registration/login.html', )


def jobrecruiter_login(request):
    if request.method == 'POST':
        try:
            password = request.POST['password']
            company_name = request.POST['company_name']
            user = authenticate(request, username=company_name, password=password)
            user_status = JobRecruiter.objects.get(user_id=user.id)
            if user is not None and user_status.is_jobrecruiter:
                login(request, user)
                return redirect('/jobrecruiter-home')
            else:
                return HttpResponse('Invalid credentials')
        except Exception:
            return HttpResponse('Invalid username or password')
    return render(request, 'registration/jobrecruiter_login.html', )


@job_recruiter_access_only()
@login_required(login_url='/jobrecruiter-login')
def create_job(request):
    if request.method == 'POST':
        title = request.POST["title"]
        description = request.POST["description"]
        author = request.user
        job_record = Job(title=title, description=description, author=author)
        job_record.save()
        return redirect("/jobrecruiter-home")

    return render(request, 'main/create_job.html')


def job_detail(request, id):
    job = Job.objects.get(id=id)
    job_application = False
    job_application_exists = JobApplication.objects.filter(job_id=id, user_id=request.user.id).exists()
    if job_application_exists:
        job_application = JobApplication.objects.get(job_id=id, user_id=request.user.id)

    if request.method == 'POST':
        resume = request.FILES.get('resume')
        application = JobApplication(resume=resume, user_id=request.user.id, recruiter_id=job.author.id, job_id=id)
        application.save()

    return render(request, 'main/job_detail.html', {'job': job, 'job_application_exists': job_application_exists,
                                                    'job_application': job_application})


@job_recruiter_access_only()
def get_job_applications(request):
    # job_applications = JobApplication.objects.all()
    # print('job_applications', job_applications)
    job_applications = {}
    job_application_exists = JobApplication.objects.filter(recruiter_id=request.user.id).exists()
    if job_application_exists:
        job_applications = JobApplication.objects.filter(recruiter_id=request.user.id)
    print('job_applications', job_applications)

    return render(request, 'main/job_applications.html', {'job_applications': job_applications})


def view_job_application(request, id):
    job_recruiter_application = False
    job_application = JobApplication.objects.get(id=id)
    job_recruiter_exists = JobRecruiter.objects.filter(user_id=request.user.id).exists()
    if job_recruiter_exists:
        job_recruiter = JobRecruiter.objects.get(user_id=request.user.id)
        if job_application.recruiter_id == job_recruiter.id:
            job_recruiter_application = True
    if request.method == 'POST':
        accept_application = request.POST["accept_application"]
        job_application.application_status = accept_application
        job_application.save()

    return render(request, 'main/view_job_application.html', {'job_application': job_application,
                                                              'job_recruiter_application': job_recruiter_application})


@job_seeker_access_only()
def get_applied_jobs(request):
    applied_jobs = {}
    job_application_exists = JobApplication.objects.filter(user_id=request.user.id).exists()
    if job_application_exists:
        applied_jobs = JobApplication.objects.filter(user_id=request.user.id)
    print('job_applications', applied_jobs)

    return render(request, 'main/applied_jobs.html', {'applied_jobs': applied_jobs})


def jobseeker_sign_up(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if JobSeeker.objects.filter(email=email).exists():
                return HttpResponse('email already exists')
            else:
                user = User.objects.create_user(username=name, email=email, password=password1)
                jobseeker_record = JobSeeker(user_id=user.id, name=name, email=email, password=password1,
                                             is_jobseeker=True)
                # user_status = UserStatus(user_id=user.id, is_jobseeker=True)
                jobseeker_record.save()
                user.save()
                # user_status.save()
                return redirect("/home")
        else:
            return HttpResponse('Pass word doesnt match')
    return render(request, 'registration/sign_up.html')


def jobrecruiter_sign_up(request):
    if request.method == 'POST':
        company_name = request.POST["company_name"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if JobRecruiter.objects.filter(email=email).exists():
                return HttpResponse('email already exists')
            else:
                user = User.objects.create_user(username=company_name, email=email, password=password1)
                jobrecruiter_record = JobRecruiter(user_id=user.id, company_name=company_name, email=email,
                                                   password=password1, is_jobrecruiter=True)
                # user_status = UserStatus(user_id=user.id, is_jobrecruiter=True)
                jobrecruiter_record.save()
                user.save()
                # user_status.save()
                return redirect("/jobrecruiter-home")
        else:
            return HttpResponse('Password doesnt match')

    return render(request, 'registration/jobrecruiter_sign_up.html')
