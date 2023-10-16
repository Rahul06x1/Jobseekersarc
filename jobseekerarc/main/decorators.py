from functools import wraps
from .models import JobSeeker, JobRecruiter
from django.shortcuts import redirect


def job_seeker_access_only():
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request, *args, **kwargs):
            jobseeker_exist = JobSeeker.objects.filter(user_id=request.user.id).exists()
            print('kkkk', jobseeker_exist)
            if not jobseeker_exist:
                return redirect('/jobseeker-login')
            return view(request, *args, *kwargs)
        return _wrapped_view
    return decorator


def job_recruiter_access_only():
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request, *args, **kwargs):
            jobrecruiter_exist = JobRecruiter.objects.filter(user_id=request.user.id).exists()
            if not jobrecruiter_exist:
                return redirect('/jobrecruiter-login')
            return view(request, *args, *kwargs)
        return _wrapped_view
    return decorator
