from django.shortcuts import get_object_or_404, render, redirect
from .models import Appointment
from patients.models import Patient
from doctors.models import Doctor
 
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'app_list.html', {'appointments': appointments})
 
 
def appointment_create(request):
    doctors = Doctor.objects.all() 
    if request.method == 'POST':
        patient = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')
        time = request.POST.get('appointment_time')
        status = request.POST.get('appointment_status')
        patient_obj, created = Patient.objects.get_or_create(name=patient)


        doctor = Doctor.objects.get(id=doctor_id)

        Appointment.objects.create(
            patient=patient_obj,
            doctor=doctor,
            time=time,
            status=status
        )

        return redirect('appointments')

    return render(request, 'app_create.html', {
        'doctors': doctors  
    })
 
 
def appointment_delete(request, id):
    appointment = Appointment.objects.get(id=id)
    appointment.delete()
    return redirect('appointments')
 
def appointment_edit(request, id):
    appointment = get_object_or_404(Appointment, pk=id)
    doctors = Doctor.objects.all()
    if request.method == 'POST':
        patient_name = request.POST.get('patient')
        patient_obj, created = Patient.objects.get_or_create(name=patient_name)
        appointment.patient = patient_obj
        appointment.doctor = Doctor.objects.get(id=request.POST.get('doctor'))
        appointment.appointment_time = request.POST.get('appointment_time')
        appointment.appointment_status = request.POST.get('appointment_status')
        appointment.save()
        return redirect('appointments')
    return render(request, 'app_edit.html', {
        'appointment': appointment,
        'doctors': doctors
    })