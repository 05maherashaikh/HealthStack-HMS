from django.shortcuts import render
from .models import Doctor
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doc_list.html', {'doctors':doctors})
