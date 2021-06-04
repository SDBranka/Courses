from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        "all_the_courses": Course.objects.all()
    }
    return render(request, "index.html", context)

def add_course(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for error in errors.values():
                messages.error(request, error)
            return redirect("/")
        else:
            Course.objects.create(
                name = request.POST["name"], 
                desc = request.POST["desc"], 
            )
            return redirect("/")   
    else:
        return redirect("/")

def destroy_check(request, course_id):
    context = {
        "this_course": Course.objects.get(id=course_id)
    }
    return render(request, "destroy_check.html", context)

def process_destroy(request, course_id):
    course_to_destroy = Course.objects.get(id=course_id)
    course_to_destroy.delete()
    return redirect("/")
