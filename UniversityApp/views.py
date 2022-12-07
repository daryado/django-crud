import copy

from django.shortcuts import render, redirect
from django.template.response import TemplateResponse

from UniversityApp.forms import UniversityForm, StudentForm
from UniversityApp.models import University, Student

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound


# Students

def student_list(request):
    all_stud = Student.objects.all()
    data = {"all_students": all_stud}
    return TemplateResponse(request, "students_table.html", data)


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        print(form.is_valid())
        if form.errors:
            for field in form:
                for error in field.errors:
                    print(field)
                    print(error)
        if form.is_valid():
            try:
                form.save()
                return redirect('/crud_app/students')
            except:
                pass
    else:
        form = StudentForm()
    return render(request, 'students_form.html', {'form': form})


def edit_student(request, id):
    if request.method == "POST":
        old_form = Student.objects.get(id=id)
        form = StudentForm(request.POST, instance=old_form)
        if form.is_valid():
            try:
                form.save()
                return redirect('/crud_app/students')
            except:
                pass
    else:
        form = Student.objects.get(id=id)
        form_new = StudentForm(instance=form)
    return render(request, 'students_form.html', {'form': form_new})


def delete_student(request, id):
    try:
        product = Student.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/crud_app/students")
    except Student.DoesNotExist:
        return HttpResponseNotFound("Student с таким id не существует")


# Universities


def universities_list(request):
    all_uni = University.objects.all()
    data = {"all_universities": all_uni}
    return TemplateResponse(request, "university_table.html", data)


def add_university(request):
    if request.method == "POST":
        form = UniversityForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/crud_app/universities')
            except:
                pass
    else:
        form = UniversityForm()
    return render(request, 'universities_form.html', {'form': form})


def edit_university(request, id):
    form = University.objects.get(id=id)
    form_new = UniversityForm(instance=form)
    return TemplateResponse(request, "universities_form.html", {'form': form_new})


def delete_university(request, id):
    try:
        uni = University.objects.get(id=id)
        uni.delete()
        return HttpResponseRedirect("/crud_app/universities")
    except University.DoesNotExist:
        return HttpResponseNotFound("University с таким id не существует")
