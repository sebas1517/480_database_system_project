# Generated by Django 4.2.7 on 2023-11-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('fname', models.CharField(db_column='Fname', max_length=45)),
                ('mi', models.CharField(db_column='MI', max_length=5)),
                ('lname', models.CharField(db_column='Lname', max_length=45)),
                ('employee_id', models.CharField(db_column='Employee_ID', max_length=45, primary_key=True, serialize=False)),
                ('age', models.IntegerField(db_column='Age')),
                ('gender', models.CharField(db_column='Gender', max_length=45)),
                ('phone_field', models.CharField(db_column='Phone#', max_length=45)),
                ('address', models.TextField(db_column='Address')),
                ('username', models.CharField(db_column='Username', max_length=45)),
                ('password', models.CharField(db_column='Password', max_length=45)),
            ],
            options={
                'db_table': 'nurse',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NurseSchedules',
            fields=[
                ('schedule_id', models.CharField(db_column='Schedule_ID', max_length=45, primary_key=True, serialize=False)),
                ('nurse_id', models.CharField(db_column='Nurse_ID', max_length=45)),
                ('time_slot', models.DateTimeField(db_column='Time_slot')),
                ('num_patients', models.IntegerField(db_column='Num_patients')),
            ],
            options={
                'db_table': 'nurse_schedules',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('fname', models.CharField(db_column='Fname', max_length=45)),
                ('mi', models.CharField(db_column='MI', max_length=5)),
                ('lname', models.CharField(db_column='Lname', max_length=45)),
                ('ssn', models.CharField(db_column='SSN', max_length=15, primary_key=True, serialize=False)),
                ('age', models.IntegerField(db_column='Age')),
                ('gender', models.CharField(db_column='Gender', max_length=15)),
                ('race', models.CharField(db_column='Race', max_length=45)),
                ('occupation_class', models.CharField(db_column='Occupation_Class', max_length=100)),
                ('medical_history_description', models.TextField(db_column='Medical_History_Description')),
                ('phone_field', models.CharField(db_column='Phone#', max_length=25)),
                ('address', models.TextField(db_column='Address')),
                ('username', models.CharField(db_column='Username', max_length=45)),
                ('password', models.CharField(db_column='Password', max_length=45)),
            ],
            options={
                'db_table': 'patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('time', models.DateTimeField(primary_key=True, serialize=False)),
                ('num_patients', models.CharField(db_column='Num_patients', max_length=45)),
                ('num_nurses', models.CharField(db_column='Num_nurses', max_length=45)),
            ],
            options={
                'db_table': 'time_slot',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VaccinationRecord',
            fields=[
                ('record_id', models.IntegerField(db_column='Record_ID', primary_key=True, serialize=False)),
                ('time_slot', models.DateTimeField(db_column='Time_slot')),
                ('patient_ssn', models.CharField(db_column='Patient_SSN', max_length=15)),
                ('nurse_id', models.CharField(db_column='Nurse_ID', max_length=45)),
                ('vaccine', models.CharField(db_column='Vaccine', max_length=50)),
                ('dosage', models.IntegerField(db_column='Dosage')),
            ],
            options={
                'db_table': 'vaccination_record',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('name', models.CharField(db_column='Name', max_length=50, primary_key=True, serialize=False)),
                ('company', models.CharField(db_column='Company', max_length=45)),
                ('num_dosages', models.IntegerField(db_column='Num_Dosages')),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('amount_available', models.IntegerField(db_column='Amount_Available')),
                ('on_hold', models.IntegerField(db_column='On_Hold')),
            ],
            options={
                'db_table': 'vaccine',
                'managed': False,
            },
        ),
    ]
