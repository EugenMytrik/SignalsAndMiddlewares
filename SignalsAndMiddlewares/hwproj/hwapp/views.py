from django.shortcuts import render
from .models import Student
from .forms import Form
import phonenumbers


def save_student(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
        name = request.POST.get('name', '')
        phone_number = request.POST.get('phone', '')
        parsed_number = phonenumbers.parse(phone_number, None)
        if phonenumbers.is_valid_number(parsed_number):
            student = Student(name=name, phone=phone_number)
            student.save()
    else:
        form = Form()
    return render(request, 'index.html', {'form': form})
