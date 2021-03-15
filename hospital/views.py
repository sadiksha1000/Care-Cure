from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Service, Doctor
from .forms import ServiceForm, DoctorForm
import os
from django.contrib import messages


def index(request):
    return HttpResponse("You succesfully reached here!!")


def home(request):
    return render(request, 'hospital/main.html')


def about(request):
    return render(request, 'hospital/about.html')


def get_service_mf(request):
    service = Service.objects.all()
    context = {
        'services': service,
        'activate_serviceMF': 'active'
    }
    return render(request, 'hospital/getServiceMF.html', context)


def post_service_mf(request):
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Service added successfully')
            return redirect('/hospital/getServiceMF/')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add service')
            return render(request, 'hospital/postServiceMF.html', {'form': form})
    context = {
        'form': ServiceForm,
        'activate_serviceMF': 'active'
    }
    return render(request, 'hospital/postServiceMF.html', context)


def update_service_mf(request, service_id):
    instance = Service.objects.get(id=service_id)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/hospital/getServiceMF')
    context = {
        'form': ServiceForm(instance=instance),
        'activate_ServiceMF': 'active'
    }
    return render(request, 'hospital/updateServiceMF.html', context)


def delete_service_mf(request, service_id):
    service = Service.objects.get(id=service_id)
    service.delete()
    return redirect('/hospital/getServiceMF')


def get_doctor_mf(request):
    doctors = Doctor.objects.all()
    context = {
        'doctors': doctors,
        'activate_doctorMF': 'active'
    }
    return render(request, "hospital/getDoctorMF.html", context)


def post_doctor_mf(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Doctor added successfully')
            return redirect('/hospital/getDoctorMF')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add doctor')
            return render(request, 'hospital/postDoctorMF.html', {'form': form})

    context = {
        'form': DoctorForm,
        'activate_doctorMF': 'active'
    }
    return render(request, 'hospital/postDoctorMF.html', context)


def view_doctor_mf(request, doctor_id):
    # doctors = Doctor.objects.get(id=doctor_id)
    # print(doctors)
    # context = {
    #     'doctors': doctors,
    #     'activate_doctorMF': 'active'
    # }
    # return render(request, 'hospital/viewDoctorMF.html', context)

    doctor = Doctor.objects.get(id=doctor_id)
    context = {
        'doctor': doctor,
        'activate_personMF': 'active'
    }
    return render(request, 'hospital/viewDoctorMF.html', context)

def edit_doctor_mf(request):
    doctors = Doctor.objects.all()
    context = {
        'doctors': doctors,
        'activate_doctorMF': 'active'
    }
    return render(request, "hospital/editDoctorMF.html", context)

def update_doctor_mf(request,doctor_id):
    instance = Doctor.objects.get(id=doctor_id)
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/hospital/getDoctorMF')
    context = {
        'form': DoctorForm(instance=instance),
        'activate_doctorMF': 'active'
    }
    return render(request, 'hospital/updateDoctorMF.html', context)

def delete_doctor_mf(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    doctor.delete()
    return redirect('/hospital/getDoctorMF')

