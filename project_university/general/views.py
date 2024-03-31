from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class Teacher:

    def work_check(request):
        return render(request, template_name='general/teacher/work_check.html', context={"fullname": "ФАМИЛИЯ И. О.",})

    def work_list(request):
        return render(request, template_name='general/teacher/work_list.html', context={"fullname": "ФАМИЛИЯ И. О.",})

    def about(request):
        return render(request, template_name='general/teacher/about.html', context={"fullname": "ФАМИЛИЯ И. О.",})


class Students:

    def get_id(request):
        return render(request, template_name='general/students/get_id.html', context={"fullname": "ФАМИЛИЯ И. О.",})

    def notification(request):
        return render(request, template_name='general/students/notification.html', context={"fullname": "ФАМИЛИЯ И. О.",})

    def progress(request):
        return render(request, template_name='general/students/progress.html', context={"fullname": "ФАМИЛИЯ И. О.",})

    def about(request):
        return render(request, template_name='general/students/about.html', context={"fullname": "ФАМИЛИЯ И. О.",})
