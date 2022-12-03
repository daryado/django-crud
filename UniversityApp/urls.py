from django.contrib import admin
from django.urls import path, include
from UniversityApp import views

urlpatterns = [

    path('students', views.student_list),
    path('students/edit', views.add_student),
    path('students/edit/<int:id>', views.edit_student),
    path('students/delete/<int:id>', views.delete_student),

    path('universities', views.universities_list),
    path('universities/edit', views.add_university),
    path('universities/edit/<int:id>', views.university_edit),
    path('universities/delete/<int:id>', views.university_delete),

    # При использовании параметров строки запроса, маршрутизация не изменяется
    #path('user/', views.user),

    #path('', views.index, name="home"),
    #path('about', views.about, name="home"),
]