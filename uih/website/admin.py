from django.contrib import admin
from .models import Patient
from .models import Nurse
from .models import NurseSchedules
from .models import TimeSlot
from .models import VaccinationRecord
from .models import Vaccine
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

admin.site.unregister(Group)
admin.site.unregister(User)

# Register your models here.

#admin.site.register(Patient)
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    ordering = ('fname',)
    search_fields = ('fname',)

#admin.site.register(Nurse)
@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    ordering = ('fname',)
    search_fields = ('fname',)

#admin.site.register(NurseSchedules)
@admin.register(NurseSchedules)
class NurseSchedulesAdmin(admin.ModelAdmin):
    list_display = ('schedule_id', 'nurse_id', 'time_slot')
    ordering = ('time_slot',)
    search_fields = ('nurse_id',)

#admin.site.register(TimeSlot)
@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    ordering = ('time',)
    search_fields = ('time',)

#admin.site.register(VaccinationRecord)
@admin.register(VaccinationRecord)
class VaccinationRecordAdmin(admin.ModelAdmin):
    list_display = ('record_id', 'time_slot', 'nurse_id')
    ordering = ('time_slot',)
    search_fields = ('record_id', 'patient_ssn',)

#admin.site.register(Vaccine)
@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'amount_available')
    ordering = ('name',)
    search_fields = ('name', 'company',)