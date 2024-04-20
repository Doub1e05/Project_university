from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


from .models import Lab
from .serializers import LabSerializer
from rest_framework.decorators import api_view


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


#---------- api ----------



@csrf_exempt

def lab_list(request):
    if request.method == 'GET':
        labs = Lab.objects.all()
        serializer = LabSerializer(labs, many = True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LabSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def lab_detail(request, pk):
    try:
        lab = Lab.objects.get(pk=pk)
    except Lab.DoesNotExist:
        return JsonResponse({'error': 'Лабораторной работы не существует'}, status=404)

    if request.method == 'GET':
        serializer = LabSerializer(lab)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LabSerializer(lab, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        lab.delete()
        return JsonResponse({'message': 'Лабораторная работа успешно удалена'}, status=204)