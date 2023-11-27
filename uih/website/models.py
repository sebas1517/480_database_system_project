# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class NurseSchedules(models.Model):
    schedule_id = models.CharField(db_column='Schedule_ID', primary_key=True, max_length=45)  # Field name made lowercase.
    nurse_id = models.CharField(db_column='Nurse_ID', max_length=45)  # Field name made lowercase.
    time_slot = models.DateTimeField(db_column='Time_slot')  # Field name made lowercase.
    num_patients = models.IntegerField(db_column='Num_patients')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nurse_schedules'


class Patient(models.Model):
    user = models.OneToOneField(User, verbose_name=("patient"), on_delete=models.CASCADE,null=True)
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
    # username = models.CharField(db_column='Username', max_length=45)  # Field name made lowercase.
    # password = models.CharField(db_column='Password', max_length=45)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'patient'


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
