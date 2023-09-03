from django.shortcuts import render

from .models import Student


# Create your views here.
def home(request):
    students = Student.objects.all().select_related("university")
    context = {"students": students}
    return render(request, "home.html", context)
