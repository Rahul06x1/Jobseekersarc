from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class Job(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    description = models.TextField()
    # slug = models.SlugField(default='', null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    is_jobseeker = models.BooleanField('jobseeker status', default=False)
    is_jobrecruiter = models.BooleanField('jobrecruiter status', default=False)

    def __str__(self):
        return self.name


class JobRecruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    is_jobseeker = models.BooleanField('jobseeker status', default=False)
    is_jobrecruiter = models.BooleanField('jobrecruiter status', default=False)

    def __str__(self):
        return self.company_name


# class UserStatus(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     is_jobseeker = models.BooleanField('jobseeker status', default=False)
#     is_jobrecruiter = models.BooleanField('jobrecruiter status', default=False)


class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(JobRecruiter, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='store/pdfs/')
    application_status = models.CharField(max_length=20, default='status_pending')
    created_at = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ['user']

    # def __str__(self):
    #     return self.user


# class Pelcon(models.Model):
#     name = models.CharField(max_length=100)
#     owner = models.CharField(max_length=100)
#     pdf = models.FileField(upload_to='store/pdfs/')
#
#     def __str__(self):
#         return self.name
