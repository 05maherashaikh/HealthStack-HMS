from django.urls import path
from .views import doctors_list, doctor_edit, doctor_delete, doctor_create

urlpatterns = [
    path('', doctors_list),
    path('<int:pk>/edit', doctor_edit),
    path('<int:pk>/delete', doctor_delete),
    path('create/', doctor_create),
]