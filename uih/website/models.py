from django.db import models
#from django.db import models, User

# Create your models here.
class Nurse(models.Model):
    fname = models.CharField(db_column='Fname', max_length=45)  # Field name made lowercase.
    mi = models.CharField(db_column='MI', max_length=5)  # Field name made lowercase.
    lname = models.CharField(db_column='Lname', max_length=45)  # Field name made lowercase.
    employee_id = models.CharField(db_column='Employee_ID', primary_key=True, max_length=45)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=45)  # Field name made lowercase.
    phone_field = models.CharField(db_column='Phone#', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    address = models.TextField(db_column='Address')  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=45)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nurse'

class Patient(models.Model):
    #user = models.OneToOneField(User, verbose_name=_("patient"), on_delete=models.CASCADE)
    fname = models.CharField(db_column='Fname', max_length=45)  # Field name made lowercase.
    mi = models.CharField(db_column='MI', max_length=5)  # Field name made lowercase.
    lname = models.CharField(db_column='Lname', max_length=45)  # Field name made lowercase.
    ssn = models.CharField(db_column='SSN', primary_key=True, max_length=15)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=15)  # Field name made lowercase.
    race = models.CharField(db_column='Race', max_length=45)  # Field name made lowercase.
    occupation_class = models.CharField(db_column='Occupation_Class', max_length=100)  # Field name made lowercase.
    medical_history_description = models.TextField(db_column='Medical_History_Description')  # Field name made lowercase.
    phone_field = models.CharField(db_column='Phone#', max_length=25)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    address = models.TextField(db_column='Address')  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=45)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient'


class NurseSchedules(models.Model):
    schedule_id = models.CharField(db_column='Schedule_ID', primary_key=True, max_length=45)  # Field name made lowercase.
    nurse_id = models.CharField(db_column='Nurse_ID', max_length=45)  # Field name made lowercase.
    time_slot = models.DateTimeField(db_column='Time_slot')  # Field name made lowercase.
    num_patients = models.IntegerField(db_column='Num_patients')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nurse_schedules'



class TimeSlot(models.Model):
    time = models.DateTimeField(primary_key=True)
    num_patients = models.CharField(db_column='Num_patients', max_length=45)  # Field name made lowercase.
    num_nurses = models.CharField(db_column='Num_nurses', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'time_slot'


class VaccinationRecord(models.Model):
    record_id = models.IntegerField(db_column='Record_ID', primary_key=True)  # Field name made lowercase.
    time_slot = models.DateTimeField(db_column='Time_slot')  # Field name made lowercase.
    patient_ssn = models.CharField(db_column='Patient_SSN', max_length=15)  # Field name made lowercase.
    nurse_id = models.CharField(db_column='Nurse_ID', max_length=45)  # Field name made lowercase.
    vaccine = models.CharField(db_column='Vaccine', max_length=50)  # Field name made lowercase.
    dosage = models.IntegerField(db_column='Dosage')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vaccination_record'


class Vaccine(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=50)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=45)  # Field name made lowercase.
    num_dosages = models.IntegerField(db_column='Num_Dosages')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    amount_available = models.IntegerField(db_column='Amount_Available')  # Field name made lowercase.
    on_hold = models.IntegerField(db_column='On_Hold')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vaccine'