from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import JobApplication


# class UploadJobApplicationForm(forms.ModelForm):
#     class Meta:
#         model = JobApplication
#         fields = ('applicant_id', 'resume',)
#
#
# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     usertype = forms.ChoiceField(choices=(
#         ("job_seeker", "Job Seeker"),
#         ("recruiter", "Recruiter"),
#     ))
#
#     class Meta:
#         model = User
#         fields = ["username", "email", "usertype", "password1", "password2"]
#
#
# class JobForm(forms.ModelForm):
#     class Meta:
#         model = Job
#         fields = ["title", "description"]
